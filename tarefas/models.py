from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    utilizador = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,)
    descricao = models.TextField(blank=True, null=True)
    concluida = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
