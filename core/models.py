from django.conf import settings
from django.db import models
from django.utils import timezone

class Capitulo(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.titulo

class Referencia(models.Model):
    titulo = models.CharField(max_length=255)
    url = models.URLField(blank=True)
    autores = models.CharField(max_length=255, blank=True)
    ano = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.titulo

class Termo(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    capitulo = models.ForeignKey(Capitulo, related_name='termos', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    termos_relacionados = models.ManyToManyField('self', blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.titulo

class Definicao(models.Model):
    termo = models.ForeignKey(Termo, related_name='definicoes', on_delete=models.CASCADE)
    texto = models.TextField()
    image_url = models.URLField(blank=True)
    referencias = models.ManyToManyField(Referencia, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Definição de {self.termo.titulo}"

class Exemplo(models.Model):
    definicao = models.ForeignKey(Definicao, related_name='exemplos', on_delete=models.CASCADE)
    descricao = models.TextField()

    def __str__(self):
        return f"Exemplo da definição de {self.definicao.termo.titulo}"
