from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Processo(models.Model):

    idf = models.PositiveSmallIntegerField(unique=True, verbose_name="IDF do Processo")
    nome = models.CharField(max_length=100, verbose_name="Nome do Processo")
    telefone = models.CharField(max_length=20, verbose_name="Telefone do Cliente do Processo", blank=True, null=True)

class Conversa(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário que criou a conversa")
    mensagem = models.CharField(max_length=350, verbose_name="O que o usuário falou na conversa")
    inicio_conversa = models.TimeField(auto_now_add=True, verbose_name="Horário de começo da conversa")
    termino_conversa = models.TimeField(verbose_name="Término da conversa")

    def encerrar_conversa(self):
        self.termino_conversa = timezone.now().time()