from django.shortcuts import render
from .models import Writing, WritingCategory

# Create your views here.
def writings(request):
    writingcategory = request.GET.get('writingcategory', '')
    if not writingcategory:
        writings = Writing.objects.all().order_by('-id')
    else:
        writings = Writing.objects.filter(category__name=writingcategory).order_by('-id')
    writingcategories = WritingCategory.objects.all().order_by('-id')
    context = {
        'writings':writings,
        'writingcategories':writingcategories
    }
    return render(request, 'writings/writings.html', context)

def writingdetail(request, slug):
    writing = Writing.objects.get(slug=slug)
    context = {
        'writing': writing
    }
    return render(request, 'writings/writingdetail.html', context)