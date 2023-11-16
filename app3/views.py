from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def kerla(request):
    return render(request,'thirdpage.html')
def kochi(request):
    return HttpResponse('<h1>nature<h1>')
