from django.contrib import admin
from .models import Produtos, Categorias

# Register your models here.
admin.site.register(Produtos)
admin.site.register(Categorias)