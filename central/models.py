from django.db import models

# Create your models here.

# classe de alunos
class AlunoTest(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=7)
    code = models.CharField(max_length=6)

    def __str__(self):
        return self.name 
