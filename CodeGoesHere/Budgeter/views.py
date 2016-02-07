from django.shortcuts import render
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
	context = {}
	return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })

def 