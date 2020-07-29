from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

tasks = ["foo", "bar", "bat"]


def index(request):
    return render(request, "tasks_todo/index.html", {
        "tasks": tasks
    })


def add(request):
    return render(request, "tasks_todo/add.html")
