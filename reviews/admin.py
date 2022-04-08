from django.contrib import admin
from .models import R_review, H_review, F_review, T_review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', )
    
admin.site.register(R_review, ReviewAdmin)
admin.site.register(H_review, ReviewAdmin)
admin.site.register(F_review, ReviewAdmin)
admin.site.register(T_review, ReviewAdmin)
