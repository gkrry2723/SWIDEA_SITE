from django.contrib import admin
from django.urls import path
from . import views

app_name = "sites"

urlpatterns = [
    path("", view= views.idea_list, name="idea_list"),
]