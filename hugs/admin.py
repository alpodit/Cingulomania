from django.contrib import admin
from .models import Hug

@admin.register(Hug)
class HugAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'timestamp')
    list_filter = ('sender', 'receiver')
    search_fields = ('sender__username', 'receiver__username')
    ordering = ('-timestamp',)
