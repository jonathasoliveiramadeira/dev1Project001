from django.db.models import QuerySet
from aula.managers import BaseManager



class ExemploManager(BaseManager):

    def find_by_nome(self, nome: str) -> QuerySet['Exemplo']:
        if isinstance(nome, str) and len(nome) > 0:
            consulta = self.filter(nome__icontains=nome)
            return consulta
        else:
            raise TypeError('O nome deve ser string')