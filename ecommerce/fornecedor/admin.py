from django.contrib import admin
from .models import Fornecedor, NovoFornecedor, AgroFornecedor

# Register your models here.

admin.site.register(Fornecedor)
admin.site.register(NovoFornecedor)
admin.site.register(AgroFornecedor)
