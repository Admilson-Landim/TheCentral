from django.db import models

# Create your models here.

# classe de alunos
class JogadorTest(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=8)
    code = models.CharField(max_length=8)
    equipa = models.CharField(max_length=30)

    def __str__(self):
        return self.name 
