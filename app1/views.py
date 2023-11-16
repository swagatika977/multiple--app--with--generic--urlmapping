from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def goa(request):
    return render(request,'firstpage.html')
def panji(request):
    return HttpResponse('<h1>capital of goa</h1')