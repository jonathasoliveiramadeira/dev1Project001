from django.core.validators import MinLengthValidator
from .base_model import BaseModel
from django.db import models
from ..enumerations import TipoEsporte


class Clube(BaseModel):
    nome = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)],
        null=False, blank=False,
        help_text="Insira o nome do clube",
        verbose_name="Nome"
    )
    local = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)],
        null=False, blank=False,
        help_text="Insira o local do clube",
        verbose_name="Local"
    )
    pais = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)],
        null=False, blank=False,
        help_text="Insira o país do clube",
        verbose_name="País"
    )
    tipo_esporte = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)],
        null=False, blank=False,
        help_text="Selecione o tipo de esporte",
        verbose_name="Tipo de esporte",
        choices=TipoEsporte,
    )
    biografia = models.TextField(
        null=True, blank=True,
        help_text="Insira a biografia",
        verbose_name="Biografia"
    )
    url = models.URLField(
        max_length=150,
        validators=[MinLengthValidator(15)],
        null=False, blank=False,
        help_text="Insira a URL",
        verbose_name="URL",
    )

    def __str__(self):
        return self.nome