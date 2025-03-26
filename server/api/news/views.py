from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView, status


class NewsView(APIView):
    def get(self, request: Request) -> Response:
        return Response(
            { "message": "OK" },
            status.HTTP_200_OK
        )

