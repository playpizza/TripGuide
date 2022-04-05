from django.contrib import admin
from .models import AdBoard

class AdAdmin(admin.ModelAdmin):
    list_display = ('title', )
    
admin.site.register(AdBoard, AdAdmin)