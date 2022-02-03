from django.contrib import admin

from .models import User, Education, Experience, JobSkills

class EducationInline(admin.TabularInline):
    model = Education
    extra = 0

class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 0
    
# class SkillsInline(admin.TabularInline):
#     model = JobSkills
#     extra = 0

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # pass
    list_display = ('first_name', 'last_name', 'email')
    fieldsets = [
        ('USER INFORMATION', {'fields': ['first_name', 'last_name', 'user_name', 'email', 'resume', 'image', 'headline', 'location'], 
                                 'classes': ['wide']}),
    ]
    inlines = [EducationInline, ExperienceInline, ]
    list_filter = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']
    list_per_page = 10

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass

@admin.register(JobSkills)
class SkillsAdmin(admin.ModelAdmin):
    extra = 1