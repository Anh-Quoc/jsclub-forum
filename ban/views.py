import imp
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

def ban(request):
    return render(request,'pages/ban.html')