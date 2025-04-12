#!/bin/sh
set -ex

echo "Ожидание MinIO..."
while ! curl -s -o /dev/null http://localhost:9000/minio/health/live; do
  sleep 1
done

echo "Настройка клиента..."
/usr/bin/mc alias set local http://localhost:9000 ${MINIO_ROOT_USER} ${MINIO_ROOT_PASSWORD} --api S3v4

echo "Создание бакета..."
/usr/bin/mc mb local/memory-site || true  # игнорируем ошибку если бакет уже существует

echo "Настройка прав доступа..."
/usr/bin/mc policy set public local/memory-site

echo "MinIO инициализирован"
