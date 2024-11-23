from flask import Flask, request, jsonify
import json
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from confluent_kafka import Producer, KafkaException
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

# Настройка Kafka Producer
kafka_config = {
    'bootstrap.servers': app.config["KAFKA_SERVERS"],
    'sasl.mechanism': app.config["KAFKA_SASL_MECHANISM"],
    'security.protocol': app.config["KAFKA_SECURITY_PROTOCOL"],
    'sasl.username': app.config["KAFKA_USERNAME"],
    'sasl.password': app.config["KAFKA_PASSWORD"]
}
producer = Producer(kafka_config)

# Отправка сообщения в Kafka
def send_to_kafka(topic, key, value):
    try:
        producer.produce(topic, key=key, value=value)
        producer.flush()
        return True
    except KafkaException as e:
        print(f"Kafka error: {e}")
        return False

# Эндпоинт для обработки файла
@app.route('/evaluate', methods=['POST'])
def evaluate_file():
    data = request.json
    if not data or "id" not in data:
        return jsonify({"error": "File ID is required"}), 400

    # Отправка в Kafka
    success = send_to_kafka(
        topic=app.config["EVALUATIONS_TOPIC"],
        key=str(data["id"]),
        value=str(data["id"])
    )

    if success:
        return jsonify({"message": "File sent for evaluation", "id": data["id"]}), 200
    else:
        return jsonify({"error": "Failed to send to Kafka"}), 500

# Эндпоинт для расчёта производительности
@app.route('/best-performance', methods=['POST'])
def best_performance():
    data = request.json
    if not data or "id" not in data:
        return jsonify({"error": "ID is required"}), 400

    # Отправка в Kafka
    success = send_to_kafka(
        topic=app.config["PERFORMANCE_TOPIC"],
        key=str(data["id"]),
        value=str(data["id"])
    )

    if success:
        return jsonify({"message": "Performance calculation request sent to Kafka", "id": data["id"]}), 200
    else:
        return jsonify({"error": "Failed to send to Kafka"}), 500

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
    app.run(host="0.0.0.0", port=5002, debug=True)
