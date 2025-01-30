FROM python:3.9
# Set environment variables
ENV PYTHONUNBUFFERED=1
COPY . /app
WORKDIR /app
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app