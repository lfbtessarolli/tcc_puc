from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Endereco(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cep = models.CharField(max_length=8, blank=True)
    rua = models.TextField(max_length=200, blank=True)
    bairro = models.TextField(max_length=50, blank=True)
    cidade = models.TextField(max_length=50, blank=True)
    estado = models.TextField(max_length=50, blank=True)
    complemento = models.TextField(max_length=200, blank=True)
    cnpj = models.CharField(max_length=18, blank=True)
    url = models.URLField(max_length=200, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Endereco.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.endereco.save()