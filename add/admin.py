from django.contrib import admin
from .models import AdBoard, AdDocument

class AdAdmin(admin.ModelAdmin):
    list_display = ('title', )
    
admin.site.register(AdBoard, AdAdmin)
admin.site.register(AdDocument, AdAdmin)