from django.db import models
from fabidecor.models import Categoria
from uploader.models import Image

class Produto(models.Model):
    adicionais = models.CharField(max_length=255)
    descricao = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=0,  null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    imagens = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="categoria"
    )

    def __str__(self):
        return self.adicionais
    

    