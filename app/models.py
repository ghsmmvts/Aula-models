from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)

# python manage.py shell

# from contas.model import Pessoa
# pessoa = Pessoa()
# pessoa.nome = 'Michel'
# pessoa.cpf = '123.123.123-12'
# pessoa.save()