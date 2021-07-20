from django.urls import path
from . import views

app_name = "sites"

urlpatterns = [
    path("", view= views.idea_list, name="idea_list"),
    path("idea", view= views.idea_list, name="idea_list"),
    path("idea/<int:pk>", view=views.idea_detail, name="idea_detail"),
    path("idea/create", view=views.idea_create, name="idea_create"),
    path("idea/edit/<int:pk>", view=views.idea_edit, name="idea_edit"),
]