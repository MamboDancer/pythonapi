# Використовуємо офіційний Python-образ
FROM python:3.11-slim

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо всі файли з поточної папки в контейнер
COPY . .

# Встановлюємо залежності, якщо вони є
RUN pip install --no-cache-dir -r requirements.txt || true

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT"]
