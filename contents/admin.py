from django.contrib import admin
from .models import Travel

class ContentsAdmin(admin.ModelAdmin):
    list_display = ('id', )
    
admin.site.register(Travel, ContentsAdmin)