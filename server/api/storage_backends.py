from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class MinioMediaStorage(S3Boto3Storage):
    def url(self, name, parameters=None, expire=None, http_method=None):
        url = super().url(
            name=name,
            parameters=parameters,
            expire=expire,
            http_method=http_method
        )
        
        url = url.replace('https://', 'http://')
        
        if settings.AWS_S3_CUSTOM_DOMAIN:
            url = url.replace(
                settings.AWS_S3_ENDPOINT_URL.rstrip('/'),
                f'http://{settings.AWS_S3_CUSTOM_DOMAIN}'.rstrip('/')
            )
        
        return url
