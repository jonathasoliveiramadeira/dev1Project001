from django.views import View

from aula.models import Person
from django.shortcuts import render

class ExemploListView(View):

    @staticmethod
    def get(request):
        persons = Person.objects.all()
        context = {
            'persons': persons,
        }
        return render(request, 'exemplo/list.html', context)


def exemplo_list(request):
    persons = Person.objects.all()
    context = {
        'persons': persons,
    }
    return render(request, 'exemplo/list.html', context)
