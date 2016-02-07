from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from Budgeter import helpers


def index(request):
	#have to change the passed parameters
	if request.user.is_authenticated():
		fromData = helpers.transactionCatagorization(request.user.get_username(), 1)
		#return render_to_response('.\Budgeter\'templates\spendanalysis.html', fromData)
		return render(request, 'spendanalysis.html', fromData)
	else:
		HttpResponseRedirect("/login")
