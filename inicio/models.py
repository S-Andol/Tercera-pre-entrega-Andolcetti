from django.db import models

# Create your models here.

class SuperHeroe(models.Model):
    nombre = models.CharField(max_length=20)
    superpoder = models.CharField(max_length=20)
    motivo = models.CharField(max_length=20)
    autor =  models.CharField(max_length=20)
