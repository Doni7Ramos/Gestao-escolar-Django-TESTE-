from django.db import models

# Create your models here.


class Professor (models.Model):
    matricula = models.IntegerField(
        default=0,
        null=False,
        blank=False 
    )

    nome = models.CharField (
        max_length=255,
        null=False,
        blank=False
    )

    cpf = models.CharField (
        max_length=11,
        null=True,
        blank=True
    )

    telefone = models.CharField (
        max_length=255,
        null=True,
        blank=True
    )
    
    email = models.EmailField (
        null=True,
        blank=True
    )

    ativo = models.BooleanField()

    formacao = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    especialidade = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )




