from django.contrib import admin

from .models import Question

@admin.register(Question)
class PetAdmin(admin.ModelAdmin):
    pass