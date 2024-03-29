from django.contrib import admin
from .models import ProjectCategory, Project
# Register your models here.

@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display=['name', 'slug']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'updated_at', 'created_at']
    
    class Media:
        js = ('js/projecttinyinject.js',)
