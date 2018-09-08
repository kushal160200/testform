from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import Form1
from . models import formdata
# Create your views here.

def form1(request):
	if request.method=='POST':
		form1=Form1(request.POST)
		if form1.is_valid():
			return render(request, 'formsapp/loginsuccess.html', {'usrname' : request.POST['usrname']})
	else:
		form1=Form1()
	return render(request, 'formsapp/formsapp.html', {'form1' : form1})
