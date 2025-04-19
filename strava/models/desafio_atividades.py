from .desafio import Desafio
from django.db import models

class DesafioAtividades(Desafio):
    meta_atividades = models.IntegerField()

    def __str__(self):
        return self.meta_atividades