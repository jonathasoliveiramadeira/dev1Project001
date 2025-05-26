from django.urls import path
import aula.views as views_funcoes
from .views import *

app_name = 'aula'

urlpatterns = [
    path('funcao/teste', views_funcoes.primeira_view, name="primeira_view"),
    #path('classe/teste', PrimeiraView.as_view(), name="primeira_view_classe"),
    #path('funcao/saudacao', views_funcoes.saudacao, name="saudacao"),

    #path('classe/teste', PrimeiraView.as_view(), name="Primera_view_class"),
    #path('classe/saudacao', SaudacaoView.as_view(), name="saudacao_view_clas"),
    #path('funcao/<str:name>', NomeView.as_view(), name="saudacao"),

    path('exemplo/function/', views_funcoes.exemplo_list,
         name="exemplo_function_list"),
    path('exemplo/classe/', ExemploListView.as_view(),
         name="exemplo_classe_list"),
]