from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Students, Courses, StudentsEnrollsToCourses, CourseCategory
from .serializers import StudentsSerializer, CoursesSerializer, StudentsEnrollsToCoursesSerializer, \
    CourseCategorySerializer
from rest_framework.filters import SearchFilter, OrderingFilter

# from snippets.permissions import IsOwnerOrReadOnly

# viewsets.ModelViewSet offers the functionality of HTTP request types.
# Only specify to get the objects from the DB.
# Create your own viewsets to change every case explicitly, but it is not usual.


class StudentsView(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (SearchFilter, OrderingFilter)
    ordering = ('student_set__date_enrolled', 'last_name', 'first_name')


class CoursesView(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer


class StudentsEnrolsToCoursesView(viewsets.ModelViewSet):
    queryset = StudentsEnrollsToCourses.objects.all()
    serializer_class = StudentsEnrollsToCoursesSerializer
    # permission_classes = (permissions.IsAuthenticated, )


class CourseCategoryView(viewsets.ModelViewSet):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer


