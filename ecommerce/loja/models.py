from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Produtos(models.Model):
	nome = models.CharField(max_length=200)
	categoria = models.TextField(default="Categoria")
	fornecedor = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	preco = models.DecimalField(max_digits=10, decimal_places=2)
	descricao = models.TextField(default="Descrição do Produto")
	atributos = models.FileField(upload_to='data/json')			#SQLite
	imagem = models.FileField(upload_to='data/img')				#SQLite
#	atributos = models.JSONField()								#PostgreSQL
#	imagem = models.ImageField()								#Postgresql
	class Meta:
		verbose_name_plural = "Produtos"

class Categorias(models.Model):
	nome = models.CharField(max_length=80)
	class Meta:
		verbose_name_plural = "Categorias"