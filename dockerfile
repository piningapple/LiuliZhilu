FROM python:3.11-slim
USER $APP_UID

WORKDIR /app
EXPOSE 8081

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8081"]
