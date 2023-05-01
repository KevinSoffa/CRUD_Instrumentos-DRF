from .serializers import InstrumentoSerializers
from rest_framework import generics
from .models import Instrumento


class InstrumentosAPIView(generics.ListCreateAPIView):
    queryset = Instrumento.objects.all()
    serializer_class = InstrumentoSerializers


class InstrumentoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instrumento.objects.all()
    serializer_class = InstrumentoSerializers



