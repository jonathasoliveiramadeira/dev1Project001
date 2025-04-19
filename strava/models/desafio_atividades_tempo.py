from .desafio import Desafio
from django.db import models

class DesafioAtividadesTempo(Desafio):
    meta_atividades = models.IntegerField()
    meta_duracao = models.TimeField()

    def __str__(self):
        return self.meta_atividades