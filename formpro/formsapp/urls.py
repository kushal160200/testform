from django.urls import include, path
from . import views

urlpatterns = [
	path('', views.form1, name='form1'),
]