from django.http import Http404
from django.shortcuts import render
from django.views import View
from aula.models import Person


class SearchView(View):
    @staticmethod
    def get(request):
        try:
            resultados = {}
            query = request.GET.get('query')
            exemplos = Person.objects.find_by_name(query)
            if len(exemplos) == 0:
                raise Http404('No exemplos')
            resultados_exemplos = []
            for exemplo in exemplos:
                url = ""
                resultados_exemplos.append((url, exemplo))
            resultados["Exemplo"] = resultados_exemplos
            context = {
                'results': resultados,
                'query': query,
            }
        except:
            context = {
                'query': query
            }
        return render(request, 'search/results.html', context)