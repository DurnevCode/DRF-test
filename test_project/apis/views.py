

from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import GeeksSerializer
from .models import GeeksModel
from rest_framework.response import Response


class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class GeeksModelViewSet(viewsets.ModelViewSet):
    serializer_class = GeeksSerializer
    parser_classes = (MultiPartParser, FormParser,)
    queryset = GeeksModel.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


