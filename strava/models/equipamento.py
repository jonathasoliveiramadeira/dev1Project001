from django.core.validators import MinLengthValidator, MinValueValidator
from .base_model import BaseModel
from django.db import models
from strava.enumerations import TipoEquipamento, TipoEsporte


class Equipamento(BaseModel):
    nome = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2)],
        null=False, blank=False,
        help_text="Insira o nome do equipamento",
        verbose_name="Nome",
    )
    marca = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2)],
        null=False, blank=False,
        help_text="Insira a marca do equipamento",
        verbose_name="Marca",
    )
    modelo = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2)],
        null=False, blank=False,
        help_text="Insira o modelo do equipamento",
        verbose_name="Modelo",
    )
    apelido = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2)],
        null=False, blank=False,
        help_text="Insira o apelido do equipamento",
        verbose_name="Apelido",
    )
    tipo_equipamento = models.CharField(
        choices=TipoEquipamento,
        null = False, blank = False,
        help_text = "Selecione o seu tipo de equipamento",
        verbose_name = "Tipo de equipamento",
    )
    tipo_esporte = models.CharField(
        choices=TipoEsporte,
        help_text="Selecione o tipo de esporte",
        verbose_name="Tipo de esporte",
    )
    distancia_total = models.FloatField(
        validators=[MinValueValidator(0)],
    )
    distancia_prevista = models.IntegerField(
        validators=[MinValueValidator(400)],
    )
    peso = models.FloatField(
        validators=[MinValueValidator(0)],
    )
    notas = models.TextField()

    def __str__(self):
        return self.nome