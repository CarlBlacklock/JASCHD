from django.conf.urls import url

from . import views
from .. import Bugeter.helpers

urlpatterns = [
	url(r'^$', views.index, name='index')
]