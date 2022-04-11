from django.contrib import admin
from .models import Board, Comment

class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', )
class CommentAdmin(admin.ModelAdmin):
    list_display = ('writer', )
    
admin.site.register(Board, BoardAdmin)
admin.site.register(Comment, CommentAdmin)