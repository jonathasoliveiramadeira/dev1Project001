from django.db import models
from .base_model import BaseModel
from .reporter import Reporter


class Article(BaseModel):
    title = models.CharField(max_length=100, help_text="Digite o tìtulo", verbose_name="Título")
    pub_date = models.DateField(help_text="Digite a data de publicação", verbose_name="Data de publicação")
    owner = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.title