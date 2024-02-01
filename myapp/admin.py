from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')

admin.site.register(MenuItem, MenuItemAdmin)
