from django.contrib import admin
from .models import Donation
# Register your models here.

@admin.register(Donation)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_of_donation', 'updated_at', 'created_at']
    
    class Media:
        js = ('js/donationtinyinject.js',)