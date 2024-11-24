# Используем Python в качестве базового образа
FROM python:3.9-slim

# Установка рабочей директории
WORKDIR /app

# Копируем зависимости
COPY Docker/imp/evaluate/requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем файлы приложения
COPY evaluate_service.py .
COPY Docker/imp/evaluate/config.json .

# Указываем порт, который будет слушать сервис
EXPOSE 5002

# Запускаем сервис
CMD ["python", "evaluate_service.py"]
