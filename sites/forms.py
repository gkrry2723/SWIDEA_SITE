from django import forms
from . import models

class IdeaForm(forms.ModelForm):
    class Meta:
        model = models.Idea
        fields = '__all__'

class ToolForm(forms.ModelForm):
    class Meta:
        model = models.Tool
        fields = '__all__'
        