from unicodedata import category
from django.shortcuts import render
from .models import Project, ProjectCategory

# Create your views here.
def projects(request):
    projectcategory = request.GET.get('projectcategory', '')
    if not projectcategory:
        projects = Project.objects.all().order_by('-id')
    else:
        projects = Project.objects.filter(category__name=projectcategory).order_by('-id')
    projectcategories = ProjectCategory.objects.all().order_by('-id')
    context = {
        'projects':projects,
        'projectcategories':projectcategories
    }
    return render(request, 'projects/projects.html', context)

def projectdetail(request, slug):
    project = Project.objects.get(slug=slug)
    context = {
        'project':project,
    }
    return render(request, 'projects/projectdetail.html', context)