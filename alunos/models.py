from django.db import models

# Create your models here.

class Aluno (models.Model):
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
    
    email = models.EmailField (
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nome
        