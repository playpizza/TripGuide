from django.contrib import admin
from .models import CountBoard

class CountAdmin(admin.ModelAdmin):
    list_display = ('reg_date', )
    
admin.site.register(CountBoard, CountAdmin)