from django.db import models
from fabidecor.models import Categoria
from uploader.models import Image

class Temas(models.Model):
    descricao = models.CharField(max_length=255)
    imagens = models.ManyToManyField(
        Image,
        related_name="+",
    )
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="fabidecor"
    )

    def __str__(self):
        return f"{self.descricao} ({self.quantidade})"

    class Meta:
        verbose_name ="Tema"