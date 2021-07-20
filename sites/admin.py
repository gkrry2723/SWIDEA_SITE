from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Idea)
class CustomIdeaAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(models.Tool)
class CustomIdeaTool(admin.ModelAdmin):
    list_display = ["name"]

