from sites.forms import IdeaForm
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

def idea_create(request):
    # 만약 create 페이지에서 create를 누르면
    if request.method == "POST":
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save()
            return redirect('sites:idea_list')
    else:
        form = IdeaForm()
        ctx = {
            'form':form
            }
        
        return render(request, template_name="ideas/idea_create.html", context = ctx)

def idea_edit(request,pk):
    idea = get_object_or_404(Idea, id=pk)
    if request.method == "POST":
        form = IdeaForm(request.POST, instance=idea)
        if form.is_valid():
            idea = form.save()
            return redirect('sites:idea_detail', pk)
    else:
        form = IdeaForm(instance=idea)
        ctx = {
            'form':form
            }
        
        return render(request, template_name="ideas/idea_create.html", context = ctx)

def idea_delete(request,pk):
    idea = get_object_or_404(Idea, id=pk)
    idea.delete()
    return redirect('sites:idea_list')