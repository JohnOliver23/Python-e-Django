from django.db import models

# Create your models here.

class Atividade(models.Model):
    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    horario = models.DateTimeField()
    lab = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return 'Atividade: {}, Autor: {}' .format(self.titulo, self.autor)

    
