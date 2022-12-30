from django.shortcuts import render


# Create your views here.
def HI(request):
    return render (request,'HI.html')
    
def HELLO(request):
    return render (request,'HELLO.html')