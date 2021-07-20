from django.shortcuts import render, redirect, get_object_or_404
from django.urls.base import reverse
from .models import Idea
from .models import Tool

# Create your views here.

def idea_list(request):
    all_ideas = Idea.objects.all()
    ctx = {
        "all_ideas":all_ideas
    }
    return render(request, template_name="ideas/idea_list.html", context=ctx)

def idea_detail(request, pk):
    idea = get_object_or_404(Idea, id=pk)
    ctx = {
        "idea":idea
    }
    return render(request, template_name="ideas/idea_detail.html", context=ctx)