from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

UserAdmin.fieldsets += ('Custom fields', {'fields': ('name', 'nickname', 'address', 'mobile', 'gender', 'age', 'is_social_login', 'is_banned')}),
admin.site.register(User, UserAdmin)