from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from truco.models import Truco
from truco.serializers import TrucoSerializer


class TrucoViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = TrucoSerializer
    queryset = Truco.objects.all()
    search_fields = ['^nomeDaMusica', '@artista', '=genero', '^link']
    filter_backends = [SearchFilter]
