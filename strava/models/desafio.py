from django.core.validators import MinLengthValidator
from .base_model import BaseModel
from django.db import models
from ..enumerations import TipoEsporte

class Desafio(BaseModel):
    nome = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(5)],
        null=False, blank=False,
        help_text="Insira qual desafio",
        verbose_name="Desafio"
    )
    data_inicio = models.DateField()
    data_fim = models.DateField()
    tipo_esporte = models.CharField(
        max_length=20,
        choices=TipoEsporte
    )
    visao_geral = models.TextField()
    selo = models.CharField(
        max_length=5
    )

    class Meta:
        abstract = True
        app_label = 'strava'

    def __str__(self):
        return self.nome