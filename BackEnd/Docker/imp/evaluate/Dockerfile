# ���������� Python � �������� �������� ������
FROM python:3.9-slim

# ��������� ������� ����������
WORKDIR /app

# �������� �����������
COPY Docker/imp/evaluate/requirements.txt .

# ������������� �����������
RUN pip install --no-cache-dir -r requirements.txt

# �������� ����� ����������
COPY evaluate_service.py .
COPY Docker/imp/evaluate/config.json .

# ��������� ����, ������� ����� ������� ������
EXPOSE 5002

# ��������� ������
CMD ["python", "evaluate_service.py"]
