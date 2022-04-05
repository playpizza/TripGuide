from django.contrib import admin
from .models import EventBoard, EventDocument

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', )
    
admin.site.register(EventBoard, EventAdmin)
admin.site.register(EventDocument, EventAdmin)