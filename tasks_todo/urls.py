from django.urls import path
from . import views

# It will be used in <a> element to link pages, used to uniquely
app_name = "tasks_todo"
# identify the urls of a particular app
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]
