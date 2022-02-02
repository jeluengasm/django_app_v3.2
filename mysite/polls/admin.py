from django.contrib import admin

from .models import Question

@admin.register(Question)
class PollsAdmin(admin.ModelAdmin):
    pass