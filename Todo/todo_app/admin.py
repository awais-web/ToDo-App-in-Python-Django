from django.contrib import admin
from .models import Tasks


@admin.register(Tasks)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ['task']