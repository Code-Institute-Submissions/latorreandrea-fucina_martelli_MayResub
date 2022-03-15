from django.contrib import admin
from .models import Account

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'user',
    )
    ordering = ('user',)
    search_fields = ['user']
admin.site.register(Account, AccountAdmin)
