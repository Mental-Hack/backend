import os
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Инициализация Flask приложения
app = Flask(__name__)

# Настройки базы данных через переменные окружения
app.config["DATABASE_URL"] = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/upload_db")

# Инициализация SQLAlchemy
Base = declarative_base()
engine = create_engine(app.config["DATABASE_URL"])
SessionLocal = sessionmaker(bind=engine)

# Таблица конфигурации
class Config(Base):
    __tablename__ = "config"
    key = Column(String, primary_key=True)
    value = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)

# Эндпоинт для получения всех настроек
@app.route("/settings", methods=["GET"])
def get_settings():
    db = SessionLocal()
    settings = db.query(Config).all()
    result = {setting.key: setting.value for setting in settings}
    db.close()
    return jsonify(result), 200

# Эндпоинт для обновления настроек
@app.route("/settings", methods=["POST"])
def update_settings():
    data = request.json
    if not data or not isinstance(data, dict):
        return jsonify({"error": "Invalid data"}), 400

    db = SessionLocal()
    try:
        for key, value in data.items():
            existing_setting = db.query(Config).filter(Config.key == key).first()
            if existing_setting:
                existing_setting.value = value
            else:
                new_setting = Config(key=key, value=value)
                db.add(new_setting)

        db.commit()
        return jsonify({"message": "Settings updated successfully"}), 200
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)
