from django import forms
from localflavor.br.forms import BRCNPJField

class DadosBasicosForm(forms.Form):
	user	 	= forms.CharField(label='Usuário', max_length=100, widget=forms.TextInput(
																attrs={
																	"value":"user.username"
																}
															)
														)
	email 		= forms.EmailField(label='E-mail', max_length=100)
	firstName 	= forms.CharField(label='Nome', max_length=100)
	lastName 	= forms.CharField(label='Sobrenome', max_length=100)
#	cnpj 		= BRCNPJField(label='CNPJ', min_length=14, max_length=18)
	cnpj 		= BRCNPJField(label='CNPJ', max_length=14, widget=forms.TextInput(
																attrs={
																	"name":"cnpj",
																	"type":"text",
																	"id":"cnpj",
																	"onfocus":"javascript: retirarFormatacao(this);",
																	"onblur":"javascript: formatarCampo(this);",																	
																	"placeholder":"00.000.000/0000-00"
																	}
																)
															)

#	def __init__(self, *args, **kwargs):
#		user = kwargs.pop('user', None)
#		super(DadosBasicosForm, self).__init__(*args, **kwargs)
#		if user is not None:
#			self.fields['board'].queryset = Board.objects.filter(user=user)