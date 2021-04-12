from django.shortcuts import render
from django.http import HttpResponse
def TestFn(request):
    return HttpResponse('helooo')
def home(request):
    return render(request,'login.html')

# Create your views here.
