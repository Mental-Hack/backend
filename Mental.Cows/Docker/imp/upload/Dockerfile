# Используем Python в качестве базового образа
FROM python:3.9-slim

# Установка рабочей директории
WORKDIR /app

# Копируем зависимости
COPY Docker/imp/upload/requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем файлы приложения
COPY upload_service.py .
COPY Docker/imp/upload/config.json .

# Указываем порт, который будет слушать сервис
EXPOSE 5001

# Запускаем сервис
CMD ["python", "files_service.py"]
