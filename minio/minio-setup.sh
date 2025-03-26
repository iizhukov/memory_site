#!/bin/sh
set -e

until (/usr/bin/mc config host add minio http://minio:9000 ${MINIO_ROOT_USER} ${MINIO_ROOT_PASSWORD}) do echo 'Waiting for MinIO...' && sleep 1; done

# Устанавливаем публичный доступ к бакету
/usr/bin/mc anonymous set public minio/news-media

