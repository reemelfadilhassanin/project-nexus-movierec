# Use official Python image
FROM python:3.11-slim


WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn


COPY . .
RUN python manage.py collectstatic --noinput

EXPOSE 8000


CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]
