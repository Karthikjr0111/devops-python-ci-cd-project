FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app/app.py"]