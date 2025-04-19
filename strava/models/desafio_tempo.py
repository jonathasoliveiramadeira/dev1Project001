from .desafio import Desafio
from django.db import models

class DesafioTempo(Desafio):
    meta_duracao = models.TimeField()

    def __str__(self):
        return f"{self.nome} - {self.meta_duracao}"