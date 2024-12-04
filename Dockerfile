# Используем официальный Python-образ
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /exchange_api

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY . .

# Команда для запуска сервера
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
