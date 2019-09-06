from django.db import models

# Create your models here.

class Truco(models.Model):
    nomeDaMusica = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    artista = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
