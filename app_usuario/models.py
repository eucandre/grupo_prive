from __future__ import unicode_literals

from django.db import models


DURACAO = ((u'Um Dia', 'Um Dia'), (u'Uma Semana', 'Uma Semana'), (u'15 Dias','15 Dias'), (u'Um Mes','Um Mes'),
	(u'Tres Meses','Tres Meses'),(u'Seis Meses', 'Seis Meses'), (u'Um Ano', 'Um Ano'))

class Plano(models.Model):
	
	nome = models.CharField(max_length=150)
	valor = models.FloatField()
	duracao = models.CharField(choices=DURACAO, max_length=150)
	descricao = models.TextField()

	def __unicode__(self):
		return self.nome

	class Meta:
		verbose_name_plurals = 'Plano Para acesso de Assinantes'	

class Usuario(models.Model):
	
	nome = models.CharField(max_length = 150)
	cpf = models.CharField(max_length=11, unique = True)
	data_nascimento = models.DateField()
	email = models.EmailField()
	plano = models.ForeignKey(Plano)

	def __unicode__(self):
		return self.nome

	class Meta:
		verbose_name_plurals = 'Assinante Cadastrado na Base do Sistema'

class Cliente(models.Model):

	nome = models.CharField(max_length = 150)
	cpf = models.CharField(max_length=11, unique = True)
	data_nascimento = models.DateField()
	email = models.EmailField()
	watsapp = models.models.CharField(max_length=11)
	web_can = models.BooleanField()
	rua = models.CharField(max_length=150)
	cidade = models.CharField(max_length=150)
	bairro = models.CharField(max_length=150)

	def __unicode__(self):
		return self.nome

	class Meta:
		verbose_name_plurals = 'Clientes que atendem aos assinantes'	

class ContaCliente(models.Model):
	cliente = models.ForeignKey(Cliente)
	valor = models.FloatField()
	pago = models.BooleanField()
	fotos = models.FileField(upload_to='/fotos/%Y/%m/%d/', blanck=True)
	videos = models.FileField(upload_to='/videos/%Y/%m/%d/', blanck=True)

	def __unicode__(self):
		return self.cliente.__str__()

	class Meta:
		verbose_name_plurals = 'Tipo de conta de Clientes'	

class ContaClienteChat(models.Model):
	'''Estou desenvolvendo o chat aqui'''
	cliente = models.ForeignKey(Cliente)
	valor = models.FloatField()
	pago = models.BooleanField()
	fotos = models.FileField(upload_to='/fotos/%Y/%m/%d/')
	videos = models.FileField(upload_to='/videos/%Y/%m/%d/')
	#chat
	def __unicode__(self):
		return self.cliente.__str__()

	class Meta:
		verbose_name_plurals = 'Tipo de conta de Clientes que podem fazer uso de chats'	
