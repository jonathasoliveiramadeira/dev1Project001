from django.db import models
from .base_model import BaseModel

class Reporter(BaseModel):
    name = models.CharField(
        max_length=100, null=False, blank=False,
        help_text="Digite o nome",
        verbose_name="Nome",
    )
    email = models.EmailField(
        help_text="Digite o email",
        verbose_name="Email",
    )
    cpf = models.CharField(
        max_length=11, null=False, blank=False,
        help_text="Digite o CPF",
        verbose_name="CPF",
    )

    def __str__(self):
        return self.name