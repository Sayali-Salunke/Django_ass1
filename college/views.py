from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def cse(request):
    return HttpResponse("welcome on CSE page")
def etc(request):
    return HttpResponse("welcome on ETC page")
def civil(request):
    return HttpResponse("welcome on CIVIL page")
def mech(request):
    return HttpResponse("welcome on MECH page")
 
    
    #return HttpResponse(b"this is string response")
    
