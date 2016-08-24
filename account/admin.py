from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Reader

# Register your models here.

admin.site.unregister(User)


@admin.register(User)
class MyUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')}
         ),
    )


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    pass
