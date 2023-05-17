FROM python:3.11-alpine
WORKDIR /app
RUN pip install --no-cache-dir bottle
COPY app.py .
CMD ["python", "app.py"]
