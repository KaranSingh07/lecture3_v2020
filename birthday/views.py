from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.


def index(request):
    today = datetime.datetime.now()

    return render(request, "birthday/birthday.html", {
        "birthday": today.day == 7 and today.month == 12
    })
