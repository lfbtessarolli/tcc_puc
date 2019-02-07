from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('fornecedor', views.FornecedorView)
router.register('novofornecedor', views.NovoFornecedorView)
router.register('agrofornecedor', views.AgroFornecedorView)

urlpatterns = [
   path('', include(router.urls)),
   path('auth/', include('rest_auth.urls')),
]