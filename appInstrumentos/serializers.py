from rest_framework import serializers
from .models import Instrumento


class InstrumentoSerializers(serializers.ModelSerializer):

    class Meta:
        model = Instrumento
        fields = (
            'id',
            'nome_instrumento',
            'marca',
            'modelo',
            'preco',
            'obs',
            'orquestra',
            'publicacao',
            'atualizacao'
        )
