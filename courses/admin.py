from django.contrib import admin

# Register your models here.
from courses.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'teachbase_id', 'name', )
