import re

from django.conf import settings


class ReplaceMinioMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if hasattr(response, 'content'):
            content = response.content.decode('utf-8')
            content = re.sub(
                r'minio:9000', 
                f'{settings.SERVER_CONFIG["DOMAIN"]}/minio',
                content
            )
            content = re.sub(
                rf'{settings.SERVER_CONFIG["IP"]}:9000',
                f'{settings.SERVER_CONFIG["DOMAIN"]}/minio', 
                content
            )
            content = re.sub(
                rf'http://{settings.SERVER_CONFIG["DOMAIN"]}/', 
                f'https://{settings.SERVER_CONFIG["DOMAIN"]}/', 
                content
            )
            response.content = content.encode('utf-8')

        return response

