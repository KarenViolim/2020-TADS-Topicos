from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Marca(models.Model):
    nome = models.CharField(max_length=80)
    descricao = models.CharField(max_length=100, verbose_name="Descrição")

    def __str__(self):
        return"{} ({})".format(self.nome, self.descricao)


class Grupo(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição")
   
    def __str__(self):
        return"{}".format(self.descricao)


class Equipamento(models.Model):
    nome_eq = models.CharField(max_length=100, verbose_name="Nome do Equipamento")
    fornecedor = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    grupo = models.ForeignKey(Grupo, on_delete=models.PROTECT)
    valor_compra = models.DecimalField(decimal_places=2, max_digits=8, verbose_name="Valor de Custo")
    valor_venda = models.DecimalField(decimal_places=2, max_digits=8, verbose_name="Valor de Venda")
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)


    def __str__(self):
        return"{} ({})".format(self.nome_eq, self.marca)

class Servico(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição")
    tipo_servico = models.CharField(max_length=50, verbose_name="Tipo do Serviço")
    valor = models.DecimalField(decimal_places=2, max_digits=6)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return"{}".format(self.descricao)

class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=120, verbose_name="Nome Cliente")
    documento = models.CharField(max_length=25, verbose_name="CPF ou CNPJ", unique=True)
    cep = models.CharField(max_length=20)
    endereco = models.CharField(max_length=120)
    numero = models.DecimalField(decimal_places=2, max_digits=4)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    celular = models.CharField(max_length=20)
    email = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return"{} ({})".format(self.nome_cliente, self.documento)    

class Funcionario(models.Model):
    nome_funcionario = models.CharField(max_length=120, verbose_name="Nome Funcionário")
    cep = models.CharField(max_length=20)
    endereco = models.CharField(max_length=120)
    numero = models.DecimalField(decimal_places=2, max_digits=4)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    celular = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return"{} ({})".format(self.nome_funcionario, self.cargo) 