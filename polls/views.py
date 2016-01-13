from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello World, you are in polls index")