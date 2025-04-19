from django.core.validators import MinLengthValidator
from .base_model import BaseModel
from django.db import models
from strava.enumerations import TipoMarca, TipoEsporte


class Record(BaseModel):
    nome = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(2)],
        null=False, blank=False,
        help_text="Nome para o Recorde",
        verbose_name="Nome",
    )
    tipo_marca = models.CharField(
        max_length=3, null=False, blank=False,
        choices=TipoMarca,
        help_text="Selecione o tipo de marca.",
        verbose_name="Tipo marca",
    )
    tipo_esporte = models.CharField(
        max_length=3, null=False, blank=False,
        choices=TipoEsporte,
        help_text="Selecione o tipo de esporte",
        verbose_name="Tipo de esporte",
    )
    ritmo = models.TimeField(
        help_text="",
        verbose_name="Ritmo",
    )
    duracao = models.DurationField(
        help_text="",
        verbose_name="Duração",
    )

    def __str__(self):
        return self.nome