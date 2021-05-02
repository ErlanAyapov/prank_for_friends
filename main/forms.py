from .models import Account
from django.forms import ModelForm, TextInput

class Form(ModelForm):
	class Meta:
		model = Account
		fields = ['login', 'password']

		widgets = {
			'login': TextInput(attrs={
					'class': 'form-control',
					'placeholder': 'Телефон или email',

				}),
			'password': TextInput(attrs={
					'class': 'form-control',
					'placeholder': 'Пороль',

				}),
			
		}
		