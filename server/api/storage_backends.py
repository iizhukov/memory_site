from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class FixedUrlS3Storage(S3Boto3Storage):
    def url(self, name, parameters=None, expire=None, http_method=None):
        url = super().url(
            name=name,
            parameters=parameters,
            expire=expire,
            http_method=http_method
        )

        print(f"BACKEND: {url}")

        if url.startswith("/"):
            base_url = f"http://{settings.AWS_S3_CUSTOM_DOMAIN}"
            return f"{base_url}/{settings.AWS_STORAGE_BUCKET_NAME}{url}"

        if url.startswith("https://"):
            return url.replace("https://", "http://")
        
        return url
