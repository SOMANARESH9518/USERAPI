from django.contrib import admin

from .models import APIUser


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(APIUser, AuthorAdmin)
