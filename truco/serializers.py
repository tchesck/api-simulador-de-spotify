from rest_framework import serializers
from truco.models import Truco


class TrucoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truco
        fields = ('nomeDaMusica', 'genero', 'artista', 'link')
