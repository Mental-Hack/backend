# ���������� Python � �������� �������� ������
FROM python:3.9-slim

# ��������� ������� ����������
WORKDIR /app

# �������� �����������
COPY Docker/imp/settings/requirements.txt .

# ������������� �����������
RUN pip install --no-cache-dir -r requirements.txt

# �������� ����� ����������
COPY settings_service.py .

# ��������� ����, ������� ����� ������� ������
EXPOSE 5003

# ��������� ������
CMD ["python", "settings_service.py"]
