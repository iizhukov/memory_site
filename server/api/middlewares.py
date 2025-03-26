import re


class ReplaceMinioMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if hasattr(response, 'content'):
            content = response.content.decode('utf-8')
            content = re.sub(
                r'http://minio:9000', 
                'http://127.0.0.1:9000', 
                content
            )
            response.content = content.encode('utf-8')
        return response

