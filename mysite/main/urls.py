# urls.py
from django.urls import path

from . import views
#This can be considered a key pair match for the routes defined in views to define the URL path for the view.

urlpatterns = [
path("<int:id>", views.index, name="index"),
path("", views.home, name="home"),
path("create/", views.create, name="index"),
path("view/", views.view, name="view"),
]