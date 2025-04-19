from django.contrib import admin
from aula.models import Person, Passport, Reporter, Article, Magazine, MagazineArticle

# Register your models here.
admin.site.register(Person)
admin.site.register(Passport)
admin.site.register(Reporter)
admin.site.register(Article)
admin.site.register(Magazine)
admin.site.register(MagazineArticle)