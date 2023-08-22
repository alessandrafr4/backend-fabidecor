from django.db import models

class Catalago(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name ="Catálogo"