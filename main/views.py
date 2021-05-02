from django.shortcuts import render, redirect
from .models import Account
from .forms import Form

def index(request):
	if request.method == 'POST':
		form = Form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')

		else:
			error = 'Дұрыс толтырылмады!'

	form = Form()

	return render(request, 'index.html', {'form':form})