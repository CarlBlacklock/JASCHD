from django.conf.urls import url

from . import views
from .. import Budgeter.helpers

urlpatterns = [
	url(r'^$', views.index, name='index')
]