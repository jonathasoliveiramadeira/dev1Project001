from django.utils.translation import gettext_lazy as _
from django.db import models

class TipoEsporte(models.TextChoices):
    RUN = "RUN", _("Corrida")
    TRAIL_RUN = "TRAIL_RUN", _("Corrida de trilhas")
    BIKE = "BIKE", _("Treino de bicicleta")
    WALK = "WALK", _("Caminhada")
    HIIT = "HIIT", _("Treino de alta intensidade")
    STRENGTH = "STRENGTH", _("Treino de força")
    CARDIO = "CARDIO", _("Treino aeróbico")
    SWIMMING = "SWIMMING", _("Natação")