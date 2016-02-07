from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from Budgeter import helpers


def index(request):
<<<<<<< HEAD
	return render(request,'useranalysis.html')
=======
	return render(request, 'savings.html')
>>>>>>> origin/master
