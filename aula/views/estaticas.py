from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from aula.models import Person
from datetime import datetime




def primeira_view(request):
    mensagem = "Boa noite DEV 1"
    #return HttpResponse(mensagem, status=200)
    return render(request, 'primeira.html', {"mensagem": mensagem})

def saudacao(request):
    agora = datetime.now()
    mensagem = "Boa noite"
    if 12 > agora.hour > 6:
        mensagem = "Bom dia"
    elif 0< agora.hour <= 6:
        mensagem = "Boa madrugada"

    completo = f"<html><body><h1>{mensagem.capitalize()} visitante!" \
               f"<br />{agora}</h1></body></html>"
    return HttpResponse(completo)


class NomeView(View):
    @staticmethod
    def get(request, name):
        exemplo = Person.objects.find_by_nome(name)
        return HttpResponse(exemplo[0], status=200)


def nome (request, name):
    exemplo = Person.objects.find_by_nome(name)
    return HttpResponse(exemplo[0], status=200)







class SaudacaoView(View):
    @staticmethod
    def get(request):
        agora = datetime.now()
        mensagem = "Boa noite"
        if 12 > agora.hour > 6:
            mensagem = "Bom dia"
        elif 0 < agora.hour <= 6:
            mensagem = "Boa madrugada"

        completo = f"<html><body><h1>{mensagem.capitalize()} visitante!" \
                   f"<br />{agora}</h1></body></html>"
        return HttpResponse(completo)



class PrimeiraView(View):
    @staticmethod
    def get(request):
        mensagem = "Boa noite DEV 1"
        return HttpResponse(mensagem, status=200)