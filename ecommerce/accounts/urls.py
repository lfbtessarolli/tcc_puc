from django.urls import path

from . import views


urlpatterns = [
    path('cadastro/', views.cadastro.as_view(), name='cadastro'),
	path('user/', views.user, name='user'),
	path('produtos/', views.produtos, name='produtos'),
	path('produtos/apiprodutos/', views.apiProdutos, name='apiprodutos'),
	path('produtos/sucess/', views.sucess, name='sucess'),
]