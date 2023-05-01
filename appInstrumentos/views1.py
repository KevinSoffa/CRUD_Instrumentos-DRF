from .serializers import InstrumentoSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Instrumento


class InstrumentoAPIView(APIView):
    '''
    API de Instrumentos feita em DRF
    '''
    def get(self, request):
        instrumentos = Instrumento.objects.all()
        serializer = InstrumentoSerializers(instrumentos, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = InstrumentoSerializers(data=request.data)
        serializer.is_valid(raise_exception=True) # Valida os dados
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)