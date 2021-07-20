from django.urls import path
from . import views

app_name = "sites"

urlpatterns = [
    path("", view= views.idea_list, name="idea_list"),
    path("idea/<int:pk>", view=views.idea_detail, name="idea_detail"),
]