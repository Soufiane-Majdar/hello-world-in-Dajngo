from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hi(request):
    if(request.method == 'POST'):
        name=request.POST['fname']
        return render(request, "sayhello/hello.html" , {'name':name})
    return render(request, "sayhello/hello.html" , {'name':"there"})
    

def homme(request):
    return render(request, "sayhello/base.html")

def getdata(request):
    return render(request, "sayhello/getData.html")