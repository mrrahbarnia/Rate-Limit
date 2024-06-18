import logging

from typing import Self, Any
from rest_framework.views import APIView
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.request import Request
from drf_spectacular.utils import extend_schema

logger = logging.getLogger('backend')


class SampleApi(APIView):

    def get(self: Self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return Response(
            {'message': 'This endpoint has not any rate limit.'},
            status=status.HTTP_200_OK
        )

class FakeLoginApi(APIView):
    """
    Redis counter =>
    key: count:/login/:{user_ip}
    value: counter: int
    ttl: sampling_period
    """
    class InputSerializer(serializers.Serializer):
        email = serializers.EmailField()
        password = serializers.CharField(max_length=25)

    @extend_schema(request=InputSerializer)
    def post(self: Self, request: Request, *args: Any, **kwargs: Any) -> Response:
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        return Response(
            {'message': 'This endpoint has rate limit.'},
            status=status.HTTP_200_OK
        )
