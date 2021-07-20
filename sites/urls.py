from django.urls import path
from . import views

app_name = "sites"

urlpatterns = [
    path("", view= views.idea_list, name="idea_list"),
    path("idea", view= views.idea_list, name="idea_list"),
    path("idea/<int:pk>", view=views.idea_detail, name="idea_detail"),
    path("idea/create", view=views.idea_create, name="idea_create"),
    path("idea/<int:pk>/edit", view=views.idea_edit, name="idea_edit"),
    path("idea/<int:pk>/delete", view=views.idea_delete, name="idea_delete"),

    path("tool", view= views.tool_list, name="tool_list"),
    path("tool/<int:pk>", view=views.tool_detail, name="tool_detail"),
    path("tool/create", view=views.tool_create, name="tool_create"),
    path("tool/<int:pk>/edit", view=views.tool_edit, name="tool_edit"),
    path("tool/<int:pk>/delete", view=views.tool_delete, name="tool_delete"),
]