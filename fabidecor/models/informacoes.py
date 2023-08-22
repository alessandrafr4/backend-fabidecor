from django.db import models

class Informacoes(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name ="informaçõe"

   
