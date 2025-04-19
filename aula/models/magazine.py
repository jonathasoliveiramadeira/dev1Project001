from django.db import models
from . import Article
from .base_model import BaseModel

class Magazine(BaseModel):
    name = models.CharField(max_length=100, help_text="Digite o nome da revista", verbose_name="Nome da revista")
    edition = models.IntegerField(help_text="Digite a edição", verbose_name="Edição")
    article = models.ManyToManyField(Article, null=True, blank=True, through="MagazineArticle", through_fields=("magazine","article"))

    def __str__(self):
        return self.name