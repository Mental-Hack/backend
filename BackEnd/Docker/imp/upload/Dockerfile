# ���������� Python � �������� �������� ������
FROM python:3.9-slim

# ��������� ������� ����������
WORKDIR /app

# �������� �����������
COPY Docker/imp/upload/requirements.txt .

# ������������� �����������
RUN pip install --no-cache-dir -r requirements.txt

# �������� ����� ����������
COPY upload_service.py .
COPY Docker/imp/upload/config.json .

# ��������� ����, ������� ����� ������� ������
EXPOSE 5001

# ��������� ������
CMD ["python", "files_service.py"]
