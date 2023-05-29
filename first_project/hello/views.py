from django.shortcuts import render
# Se imporata HTTPResponse 
from django.http  import HttpResponse

# Create your views here.
def index (request):
   return HttpResponse("Hola desde mi primera vista ⭐")
def author (request):
   return HttpResponse("Autor: Guizar Mario 😎")
