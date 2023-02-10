from django.db import models

# Create your models here.

class comentarios(models.Model):
    title = models.CharField(max_length=50)
    comentario = models.CharField(max_length=100)
    reaccion = models.CharField(max_length=50)
    fecha = models.PositiveBigIntegerField()

    #def __str__(self):
        #return (self.title)
