
from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=150)
    nacionalidade = models.CharField(max_length=100, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Genero(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        related_name='livros'
    )
    genero = models.ForeignKey(
        Genero,
        on_delete=models.CASCADE,
        related_name='livros'
    )
    ano_publicacao = models.PositiveIntegerField()
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.titulo
