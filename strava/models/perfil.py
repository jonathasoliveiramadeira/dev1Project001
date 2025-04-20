from django.core.validators import MinLengthValidator, MinValueValidator
from .base_model import BaseModel
from django.db import models
from strava.enumerations import Genero
from django.utils.timezone import now
# from django.views.generic.dates import timezone_today


class Perfil(BaseModel):
    email = models.EmailField(
        max_length=100,
        validators=[MinLengthValidator(10)],
        null=False, blank=False,
        help_text="Insira seu Email",
        verbose_name="Email",
    )
    nome = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(10)],
        null=False, blank=False,
        help_text="Insira seu nome",
        verbose_name="Nome",
    )
    cpf = models.CharField(
        max_length=11,
        null=False, blank=False,
        help_text="Insira seu CPF",
        verbose_name="CPF",
    )
    senha = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(5)],
        null=False, blank=False,
        help_text="Insira sua senha",
        verbose_name="Senha",
    )
    data_nascimento = models.DateField(
        help_text="Qual sua data de nascimento?",
        verbose_name="Data de nascimento",
    )
    local = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)],
        help_text="Insira seu local",
        verbose_name="Local"
    )
    pais = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)],
        help_text="Insira seu País",
        verbose_name="País"
    )
    genero = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(3)],
        null=False, blank=False,
        choices=Genero,
        help_text="Selecione o seu gênero",
        verbose_name="Gênero"
    )
    peso = models.FloatField(
        validators=[MinValueValidator(20)],
        default=0.00, null=True, blank=True,
        help_text="Insira seu peso",
        verbose_name="Peso",
    )
    pagina_pessoal = models.URLField(
        max_length=150,
        validators=[MinLengthValidator(15)],
        null=False, blank=False,
        help_text="Insira sua URL",
        verbose_name="URL",
    )
    biografia = models.TextField(
        null=True, blank=True,
        help_text="Insira sua biografia",
        verbose_name="Biografia"
    )
    premium = models.BooleanField(default=False)
    membro_desde = models.DateField(
        default=now
    )

    def __str__(self):
        return self.nome