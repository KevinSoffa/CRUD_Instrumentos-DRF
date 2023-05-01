from .views import InstrumentoAPIView, InstrumentosAPIView
from django.urls import path


urlpatterns = [
    path('instrumentos/', InstrumentosAPIView.as_view(), name='instrumentos'),
    path('instrumentos/<int:pk>/', InstrumentoAPIView.as_view(), name='instrumento')
]
