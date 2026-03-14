FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install flask pytest

EXPOSE 5000

CMD ["python", "app/app.py"]