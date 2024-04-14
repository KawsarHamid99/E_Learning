from django.contrib import admin
from .models import Course,Enrollment
# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=["id"]

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display=["id"]
