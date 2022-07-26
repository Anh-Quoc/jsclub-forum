import imp
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

def event(request):
    return render(request,'pages/event.html')
