from django.shortcuts import render
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from Budgeter import models
from django.contrib.auth.models import User
import Budgeter.helpers as h

class UserDataForm(forms.Form):
    #income = forms.DecimalForms()
    transactions = forms.FileField()


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
            form = UserDataForm(request.FILES)
            f2 = open(request.POST['transactions'], 'r')
            
            raw_transactions = h.getTransactionsFromFile(f2.read())
            f.close()
            h.transactionFormatAndSave(raw_transactions, username)
            return HttpResponse("/spendingAnalysis")
        else:
            form = UserDataForm()
        return render(request, 'useranalysis.html', {'form': form})
    else:
        return HttpResponseRedirect("/login")