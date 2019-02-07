from rest_framework import serializers
from .models import Fornecedor, NovoFornecedor, AgroFornecedor

class FornecedorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Fornecedor
		fields = (
			'nome', 
			'categoria',  
			'preco', 
			'descricao', 
			'atributos', 
			'imagem'
			)

class NovoFornecedorSerializer(serializers.ModelSerializer):
	class Meta:
		model = NovoFornecedor
		fields = (
			'nome', 
			'categoria',  
			'preco', 
			'descricao', 
			'atributos', 
			'imagem'
			)
			
class AgroFornecedorSerializer(serializers.ModelSerializer):
	class Meta:
		model = AgroFornecedor
		fields = (
			'nome', 
			'categoria',  
			'preco', 
			'descricao', 
			'atributos', 
			'imagem'
			)