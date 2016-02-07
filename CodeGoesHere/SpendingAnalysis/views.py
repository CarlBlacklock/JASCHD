from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from Budgeter import helpers

#have to change the passed parameters
from_database = helpers.transactionCatagorization(1, 1)

#food = from_database[0]
#ent = from_database[1]
#elec = from_database[2]
#oFood = from_database[3]
#clo = from_database[4]
#tra = from_database[5]

def index(request):
	return render(request, '.\Budgeter\'templates\useranalysis.html')