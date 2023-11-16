from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def puri(request):
    return render(request,'secondpage.html')
def balagandi(request):
    return HttpResponse('<h1> GUNDICHA TEMPLE</h1>')