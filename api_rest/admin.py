from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'user_email', 'user_age')
admin.site.register(User)

