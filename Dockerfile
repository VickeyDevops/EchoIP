FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]
# Expose the port the app runs on
EXPOSE 5000
# Set environment variables

