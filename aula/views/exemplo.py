from django.urls.base import reverse_lazy
from django.views import View
from django.views.generic import DeleteView
from aula.models import Person
from django.shortcuts import render, redirect, get_object_or_404


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

def exemplo_detail(request, pk):
    exemplo = Person.objects.get(id=pk)
    context = {
        'exemplo': exemplo,
    }
    return render(request, 'exemplo/read.html', context)

class ExemploDetailView(View):

    @staticmethod
    def get(request, pk):
        persons = Person.objects.all()
        context = {
            'persons': persons,
        }
        return render(request, 'exemplo/list.html', context)

def delete(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    print(person_id)
    try:
        if request.method == 'POST':
            v_exemplo_id = request.POST.get("person_id", None)
            if int(v_exemplo_id) == person_id:
                person.delete()
                return redirect('aula:exemplo_function_list')
        else:
            context = {
                'exemplo': person,
            }
            return render(request, 'exemplo/delete.html', context)
    except:
        context = {}
        return render(request, 'exemplo/list.html', context)

class ExemploDeleteView(DeleteView):
    model = Person
    fields = '__all__'
    template_name = "exemplo/delete_classe.html"
    success_url = reverse_lazy('aula:exemplo_classe_list')