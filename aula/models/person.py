import random
import string

from django.core.exceptions import ValidationError
from django.db import models
from .base_model import BaseModel
from aula.validators import validate_par
from ..managers.person import PersonManager


class Person(BaseModel):
    name = models.CharField(
        max_length=100, null=False, blank=False,
        help_text="Digite o nome",
        verbose_name="Nome",
    )
    birth_date = models.DateField(

    )
    cpf = models.CharField(
        max_length=11, null=False, blank=False,
        help_text="Digite o CPF",
        verbose_name="CPF",
        validators=[validate_par],
    )

    objects = PersonManager()

    # Qualquer coisa que eu queira altera antes de salvar
    def save(self, *args, **kargs):
        if self.name is None or self.name == '':
            letters = string.ascii_letters + string.digits
            self.name = ''.join(random.choice(letters) for i in range(10))
        super().save(*args, **kargs)

    def __str__(self):
        return self.name

    def clean(self):
        # Pode ser realizada aqui novas validações
        if not isinstance(str(self.name), str):
            raise ValidationError({"nome": 'Nome informado é do tipo errado'},
                                  code="error001")
        elif self.name == "Teste":
            raise ValidationError(
                {"nome": 'Não é possível salvar testes!'},
                code="error002")
        elif (self.cpf == "11111111111" and self.name == "IFRS Restinga"):
            raise ValidationError(
                {"nome": 'Combinação de nome e codigo errada!',
                 "cod": 'Combinação de nome e código errada!'},
                code="error0101")
