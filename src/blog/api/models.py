from django.db import models

# Create your models here.
class EntradaModel(models.Model):
    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    cuerpo = models.TextField(max_length=200)

    def __str__(self):
        return self.titulo