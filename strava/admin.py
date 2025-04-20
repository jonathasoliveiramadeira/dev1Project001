from django.contrib import admin
from strava.models import Atividade, Equipamento, Record, Clube, Perfil

# Register your models here.
admin.site.register(Atividade)
admin.site.register(Clube)
admin.site.register(Equipamento)
admin.site.register(Perfil)
admin.site.register(Record)
