from django.contrib import admin

from fabidecor.models import  Categoria, Informacoes, Temas, Catalago

admin.site.register(Categoria)
admin.site.register(Informacoes)
admin.site.register(Temas)
admin.site.register(Catalago)

from django.contrib import admin