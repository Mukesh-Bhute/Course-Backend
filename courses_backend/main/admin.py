from django.contrib import admin
from .models import Course, CourseInstance

# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'course_code', 'description')
    search_fields = ('title', 'course_code')

@admin.register(CourseInstance)
class CourseInstanceAdmin(admin.ModelAdmin):
    list_display = ('course', 'year', 'semester')
    list_filter = ('year', 'semester')
    search_fields = ('course__title', 'year', 'semester')
