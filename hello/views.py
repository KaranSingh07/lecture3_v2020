from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Hello, world!")


def karan(request):
    return HttpResponse("Hello, karan!")


def brian(request):
    return HttpResponse("Hello, brian!")


def greet(request, name):
    # Simple way (Just python syntax for formatted syntax)
    # return HttpResponse(f"Hello, {name.capitalize()}!")

    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
    # Passing values to the html file, using a dictionary, this is called context.


def renderHtmlFile(request):
    return render(request, "hello/index.html")
