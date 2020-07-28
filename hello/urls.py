from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("karan", views.karan, name="karan"),
    path("htmlfile", views.renderHtmlFile, name="htmlfile"),
    path("brian", views.brian, name="brian"),
    path("<str:name>", views.greet, name="greet")
]
