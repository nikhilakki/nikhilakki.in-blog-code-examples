FROM python:3.11.6-slim
WORKDIR /app
# Install Python modules
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# Copy all source files to container
COPY . .
CMD ["python", "./main.py"]