from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Students', views.StudentsView)
router.register('Courses', views.CoursesView)
router.register('StudentsEnrollsToCourses', views.StudentsEnrolsToCoursesView)
router.register('CourseCategory', views.CourseCategoryView)

urlpatterns = [
    path('', include(router.urls))
]