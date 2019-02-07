from django.shortcuts import render
from rest_framework import viewsets
from .models import Fornecedor, NovoFornecedor, AgroFornecedor
from .serializers import FornecedorSerializer, NovoFornecedorSerializer, AgroFornecedorSerializer
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required
class FornecedorView(viewsets.ModelViewSet):
	queryset = Fornecedor.objects.all()
	serializer_class = FornecedorSerializer
	
class NovoFornecedorView(viewsets.ModelViewSet):
	queryset = NovoFornecedor.objects.all()
	serializer_class = NovoFornecedorSerializer
	
class AgroFornecedorView(viewsets.ModelViewSet):
	queryset = AgroFornecedor.objects.all()
	serializer_class = AgroFornecedorSerializer