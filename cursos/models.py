from django.db import models

# Create your models here.

class Curso (models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    codigo = models.IntegerField(
        default=0,
        null=False,
        blank=False 
    )

    classificacao = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    ativo = models.BooleanField()
    
    classificacao = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

