from django.utils.translation import gettext_lazy as _
from django.db import models

class TipoMarca(models.TextChoices):
    TP100M = "100M", _("100 metros")
    TP400M = "400M", _("400 metros")
    TP1KM = "1KM", _("1 quilômetro")
    TP5KM = "5KM", _("5 quilômetros")
    TP10KM = "10KM", _("10 quilômetros")
    TP15KM = "15KM", _("15 quilômetros")
    TP20KM = "20KM", _("20 quilômetros")
    MEIA = "MEIA", _("Meia maratona")
    TP30KM = "30KM", _("30 quilômetros")
    MARATONA = "MARATONA", _("Maratona")
    LONGA_DISTANCIA = "LONGA_DISTANCIA", _("Maior distância")
    LONGA_DURACAO = "LONGA_DURACAO", _("Maior duração")