from django.contrib import admin
from .models import Students, Courses, CourseCategory, StudentsEnrollsToCourses

admin.site.register(Students)
admin.site.register(Courses)
admin.site.register(CourseCategory)
admin.site.register(StudentsEnrollsToCourses)


# delet= StudentsEnrollsToCourses.objects.all()
# delet.delete()
