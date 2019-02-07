from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required, user_passes_test
import requests
# from .forms import DadosBasicosForm
from .models import Endereco
from loja.models import Produtos

class cadastro(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/cadastro.html'
	
@login_required
def user(request):
	if request.method == 'POST':
#		print(request.POST)
		user_id = int(request.user.id)
		up_user = User.objects.get(pk=user_id)
		up_first = request.POST.get('firstname')
		up_email = request.POST.get('email')
		up_cnpj = request.POST.get('cnpj')
		up_url = request.POST.get('url')
		up_cep = request.POST.get('cep')
		up_rua = request.POST.get('rua')
		up_bairro = request.POST.get('bairro')
		up_cidade = request.POST.get('cidade')
		up_uf = request.POST.get('uf')
		up_comp = request.POST.get('complemento')
		User.objects.select_related().filter(id=user_id).update(
								first_name=up_first,
								email=up_email
								)

		Endereco.objects.select_related().filter(user=up_user).update(
								cnpj=up_cnpj,
								url=up_url,
								cep=up_cep,
								rua=up_rua,
								bairro=up_bairro,
								cidade=up_cidade,
								estado=up_uf,
								complemento=up_comp
								)

	context = {
		'title'		: 'Área do Usuário'
	}

	return render(request, 'registration/user.html/', context)

@user_passes_test(lambda u: u.groups.filter(name='Fornecedor').exists())	
@login_required
def produtos(request):
	user_id = int(request.user.id)
	produtos = Produtos.objects.filter(fornecedor=user_id)
	url = Endereco.objects.get(user=user_id)
	context = {
		'title'		: 'Produtos do Usuário',
		'produtos'	: produtos,
		'url'		: url,
	}

	return render(request, 'registration/produtos.html/', context)

@user_passes_test(lambda u: u.groups.filter(name='Fornecedor').exists())
@login_required
def apiProdutos(request):
	user_id = int(request.user.id)	
	url = Endereco.objects.get(user=user_id)
	response = requests.get(url.url)
	data = response.json()
	if response.status_code != 200:
		data = ''
	else:
#		print(response)
		data = response.json()
#		for each in data:
#			n_nome = each['nome']
#			print(n_nome)		
	context = {
		'title'		: 'API do Usuário',
		'data'		: data,
	}

	return render(request, 'registration/apiprodutos.html/', context)

@user_passes_test(lambda u: u.groups.filter(name='Fornecedor').exists())
@login_required
def sucess(request):
	user_id = int(request.user.id)
	produtos = Produtos.objects.filter(fornecedor=user_id)
	produtos.delete()
	url = Endereco.objects.get(user=user_id)
	if request.method == 'POST':
		response = requests.get(url.url)
		data = response.json()
		for each in data:
			n_nome = each['nome']
			n_cat = each['categoria']
			n_preco = each['preco']
			n_desc = each['descricao']
			n_atrb = each['atributos']
			n_atrb = n_atrb[27:]		#SQLite
			n_img = each['imagem']
			n_img = n_img[27:]			#SQLite
			n_user = User.objects.get(pk=user_id)
			Produtos.objects.create(
								nome=n_nome,
								categoria=n_cat,
								fornecedor=n_user,
								preco=n_preco,
								descricao=n_desc,
								atributos=n_atrb,
								imagem=n_img								
								)
	context = {
		'title'		: 'Sucesso na atualização do catálogo'
	}

	return render(request, 'registration/sucess.html/', context)