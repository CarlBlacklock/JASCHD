from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from Budgeter import helpers


def index(request):
	return render(request, '.\Budgeter\'templates\useranalysis.html')
