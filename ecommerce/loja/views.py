from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Produtos, Categorias

# Create your views here.
def index(request):

	produtos = Produtos.objects.all()[:40]
	
	context = {
		'title' : 'Listagem de Produtos',
		'produtos' : produtos
	}

	return render(request, 'loja/index.html/', context)

def details(request, id):

	prods = Produtos.objects.get(pk=id)
	
	context = {
		'title' : 'Detalhe do Produto',
		'prods' : prods
	}
	
	return render(request, 'loja/details.html/', context)	