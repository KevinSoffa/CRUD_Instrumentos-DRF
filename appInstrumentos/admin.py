from django.contrib import admin
from .models import Instrumento


@admin.register(Instrumento)
class InstrumentoAdmin(admin.ModelAdmin):
    list_display = (
        'nome_instrumento',
        'marca',
        'modelo',
        'preco',
        'obs',
        'orquestra'
    )
