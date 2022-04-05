from django.contrib import admin
from .models import EventBoard

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', )
    
admin.site.register(EventBoard, EventAdmin)