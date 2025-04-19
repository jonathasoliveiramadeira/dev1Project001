from django.db import models
from .base_model import BaseModel
from .person import Person

class Passport(BaseModel):
    number = models.CharField(
        max_length=100, null=False, blank=False,
        help_text="Digite o número",
        verbose_name="Número",
    )
    issue_date = models.DateField(help_text="Digite a data de emissão", verbose_name="Data de emissão")
    expiration_date = models.DateField(help_text="Digite a data de expiração", verbose_name="Data de expiração")
    owner = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.number
