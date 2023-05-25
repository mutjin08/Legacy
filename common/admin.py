from django.contrib import admin
from .models import CustomGroup


class CustomGroupAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(CustomGroup, CustomGroupAdmin)
