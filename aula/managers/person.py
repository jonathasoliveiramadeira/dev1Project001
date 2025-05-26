from django.db.models import QuerySet
from aula.managers import BaseManager



class PersonManager(BaseManager):

    def find_by_name(self, name: str) -> QuerySet['Person']:
        if isinstance(name, str) and len(name) > 0:
            consulta = self.filter(name__icontains=name)
            return consulta
        else:
            raise TypeError('O nome deve ser string')