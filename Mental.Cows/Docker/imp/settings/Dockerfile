# Используем Python в качестве базового образа
FROM python:3.9-slim

# Установка рабочей директории
WORKDIR /app

# Копируем зависимости
COPY Docker/imp/settings/requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем файлы приложения
COPY settings_service.py .

# Указываем порт, который будет слушать сервис
EXPOSE 5003

# Запускаем сервис
CMD ["python", "settings_service.py"]
