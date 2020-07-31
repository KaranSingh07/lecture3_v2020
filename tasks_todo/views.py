from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New task")
    # priority = forms.IntegerField(label="Priority", min_value=0, max_value=10)


def index(request):
    # If user doesn't have a list of task, create one for them...
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks_todo/index.html", {
        "tasks": request.session["tasks"]
    })


def add(request):
    if request.method == "POST":            # If method is post, process it...
        # Then get the form from POST method
        form = NewTaskForm(request.POST)
        if form.is_valid():                 # If form is valid,
            # Get the task input and append it to the list.
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]

            return HttpResponseRedirect(reverse("tasks_todo:index"))
            # Or simply HttpResponseRedirect(reverse("/tasks_todo")
            # We use reverse method just to not hardcode the URL, [app_name:view]

        else:               # If form is invalid, resend the filled form to show errors.
            return render(request, "tasks_todo/add.html", {
                "form": form
            })
            # If method is not POST, render empty form...
    return render(request, "tasks_todo/add.html", {
        "form": NewTaskForm()
    })
