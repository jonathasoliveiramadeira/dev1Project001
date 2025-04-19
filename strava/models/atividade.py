from django.core.validators import MinLengthValidator, MinValueValidator
from .base_model import BaseModel
from django.db import models
from ..enumerations import TipoEsporte

class Atividade(BaseModel):
    nome = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(5)],
        null=False, blank=False,
        help_text="Insira o nome da atividade",
        verbose_name="Nome",
    )
    observacoes = models.CharField(
        max_length=100,
        null=True, blank=True,
        help_text="Insira as observações",
        verbose_name="Observações"
    )
    data = models.DateField()
    tipo_esporte = models.CharField(
        choices=TipoEsporte,
        help_text="Selecione o tipo de esporte",
        verbose_name="Tipo de esporte"
    )
    inicio = models.TimeField()
    duracao = models.DurationField()
    distancia = models.FloatField()
    ritmo = models.TimeField()
    calorias = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=0,
    )
    elevacao_total = models.IntegerField(default=0)

    def __str__(self):
        return self.nome