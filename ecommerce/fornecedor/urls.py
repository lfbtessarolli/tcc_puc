from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register('fornecedor', views.FornecedorView)
router.register('novofornecedor', views.NovoFornecedorView)
router.register('agrofornecedor', views.AgroFornecedorView)

urlpatterns = [
   path('', include(router.urls)),
   path('auth/', include('rest_auth.urls')),
   path('docs/', include_docs_urls(title='API Fornedor')),
]