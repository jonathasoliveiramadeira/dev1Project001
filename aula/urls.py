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
    path('exemplo/function/read/<int:pk>/', views_funcoes.exemplo_detail,
         name="exemplo_function_read"),
    path('exemplo/classe/read/<int:pk>/', ExemploDetailView.as_view(),
         name="exemplo_classe_read"),
    path('exemplo/function/delete/<int:person_id>', views_funcoes.delete,
         name="exemplo_function_delete"),
    path('exemplo/classe/delete/<int:pk>', ExemploDeleteView.as_view(),
         name="exemplo_classe_delete"),
]