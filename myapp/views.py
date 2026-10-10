from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
def index(request):
    return render(request, "hello/index.html")

def alan(request):
    return HttpResponse("<h2>Hello, Alan<h2>")

def ikuzwe(request):
    return HttpResponse("<h3>Hello, Ikuzwe</h3>")

def greet(request, name):
    return render(request, "hello/greet.html",{
        "name": name.capitalize()
    })