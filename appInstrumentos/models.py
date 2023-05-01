from django.db import models


class Base(models.Model):
    publicacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Instrumento(Base):
    nome_instrumento = models.CharField(
        max_length=255
    )
    marca = models.CharField(
        max_length=255
    )
    modelo = models.CharField(
        max_length=255
    )
    preco = models.FloatField()
    obs = models.CharField(
        max_length=255
    )
    orquestra = models.BooleanField(
        default=True
    )
    
    class Meta:
        verbose_name = 'Instrumento'
        verbose_name_plural = 'Instrumentos'

    def __str__(self):
        return f'{self.nome_instrumento} | {self.marca}'
