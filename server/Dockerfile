FROM python:3.13-slim AS builder

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Final build
FROM python:3.13-slim

COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN apt-get update && apt-get install -y \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

RUN if [ -f ".env.docker" ]; then \
        cp .env.docker .env; \
    elif [ -f ".env.prod" ]; then \
        cp .env.prod .env; \
    else \
        echo "Neither .env.docker nor .env.prod found!" >&2; \
        exit 1; \
    fi

ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=config.settings

EXPOSE 8000

RUN echo "#!/bin/bash\n" \
    "python manage.py migrate --noinput\n" \
    "python manage.py createsuperuser --noinput --username admin123 --email admin123@example.com || true\n" \
    "python manage.py runserver 0.0.0.0:8000\n" > /app/entrypoint.sh \
    && chmod +x /app/entrypoint.sh

ENV DJANGO_SUPERUSER_PASSWORD=admin123

CMD ["/app/entrypoint.sh"]
