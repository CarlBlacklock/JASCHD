from django.shortcuts import render
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from Budgeter import models
from django.contrib.auth.models import User

class UserDataForm(forms.Form):
    #income = forms.DecimalForms()
    transactions = forms.FileField()


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

def importUserData(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            username = request.user.get_username()
            form = UserDataForm(request.POST, request.FILES)
            if form.is_valid():
                handle_uploaded_file(request.FILES['transactions'])
                return HttpResponseRedirect("/spendingAnalysis")
        else:
            form = UserDataForm()
        return render(request, 'useranalysis.html', {'form': form})
    else:
        return HttpResponseRedirect("/login")

def handle_uploaded_file(file):
    with open('..\\..\\Userdata\\newFile', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)