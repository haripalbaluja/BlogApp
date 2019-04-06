from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
	#return HttpResponse("Home")
	return render(request,'homepage.html')

def about(request):
	#return HttpResponse("about Haripal")
	return render(request,'about.html')