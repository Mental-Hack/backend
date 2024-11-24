import os
import asyncio
import aiofiles
import json
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from authlib.integrations.flask_oauth2 import ResourceProtector
from authlib.oauth2.rfc6749.errors import InvalidTokenError
from authlib.oauth2.rfc6749 import BearerTokenValidator

# Загрузка дефолтного конфига
with open("config.json", "r") as config_file:
    DEFAULT_CONFIG = json.load(config_file)

# Flask приложение
app = Flask(__name__)

# Настройки из дефолтного конфига
app.config.update(DEFAULT_CONFIG)

# База данных
Base = declarative_base()
engine = create_engine(app.config["DATABASE_URL"])
SessionLocal = sessionmaker(bind=engine)

# Таблица конфигурации
class Config(Base):
    __tablename__ = "config"
    key = Column(String, primary_key=True)
    value = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)

# Загрузка настроек из БД
def load_config_from_db():
    db = SessionLocal()
    db_config = db.query(Config).all()
    if db_config:
        for entry in db_config:
            app.config[entry.key] = entry.value
    db.close()

# Применение конфигурации из БД при старте
load_config_from_db()

# Создаём папку для загрузки файлов
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# Асинхронная загрузка файлов
@app.route("/upload", methods=["POST"])
async def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    # Сохранение файла
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    try:
        async with aiofiles.open(file_path, "wb") as f:
            await f.write(file.read())
        return jsonify({"message": "File uploaded successfully", "path": file_path}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Эндпоинт для изменения конфигурации
@app.route("/config", methods=["POST"])
def update_config():
    data = request.json
    if not data or not isinstance(data, dict):
        return jsonify({"error": "Invalid config data"}), 400

    db = SessionLocal()
    try:
        for key, value in data.items():
            # Обновляем или вставляем настройку в таблицу
            existing_entry = db.query(Config).filter(Config.key == key).first()
            if existing_entry:
                existing_entry.value = value
            else:
                new_entry = Config(key=key, value=value)
                db.add(new_entry)

            # Обновляем настройки в приложении
            app.config[key] = value

        db.commit()
        return jsonify({"message": "Configuration updated successfully"}), 200
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
