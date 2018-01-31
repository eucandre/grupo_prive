from django import forms
from .models import *

class FormPlano(forms.ModelForm):
	class Meta:
		model = Plano
		fields = ('nome','valor','duracao','descricao')

class FormUsuario(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = ('nome','cpf','data_nascimento','email','plano')

class FormCliente(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = ('nome','cpf','data_nascimento','email','watsapp','web_can','rua','cidade','bairro')


class FormContaCliente(forms.ModelForm):
	class Meta:
		model = ContaCliente
		fields = ('cliente','valor','pago','fotos','videos')

class FormContaClienteChat(forms.ModelForm):
	class Meta:
		model = ContaClienteChat
		fields = ('cliente','valor','pago','fotos','videos')
