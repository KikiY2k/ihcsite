from django.contrib import admin
from .models import Termo, Referencia, Definicao, Exemplo, Capitulo

admin.site.register(Termo)
admin.site.register(Referencia)
admin.site.register(Definicao)
admin.site.register(Exemplo)
admin.site.register(Capitulo)