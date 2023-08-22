from django.db import models

from fabidecor.models import Categoria


class Temas(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    quantidade = models.IntegerField(default=0,  null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="livros"
    )

    def __str__(self):
        return f"{self.titulo} ({self.quantidade})"

    class Meta:
        verbose_name ="Tema"