from django.contrib import admin
from .models import WritingCategory, Writing
# Register your models here.

@admin.register(WritingCategory)
class WritingCategoryAdmin(admin.ModelAdmin):
    list_display=['name', 'slug']

@admin.register(Writing)
class WritingAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'updated_at', 'created_at']

    class Media:
        js = ('js/writingtinyinject.js',)
