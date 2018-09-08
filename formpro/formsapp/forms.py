from django import forms

class Form1(forms.Form):
	usrname=forms.CharField(label="Username", max_length=100)
	password=forms.CharField(max_length=100, widget=forms.PasswordInput)
