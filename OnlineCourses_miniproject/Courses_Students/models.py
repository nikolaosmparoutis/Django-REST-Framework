from django.db import models

#TODO from django.contrib.auth.models import User


class Students(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    occupation = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + self.last_name


class CourseCategory(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Courses(models.Model):
    course_name = models.CharField(max_length=50)
    course_tutor_fname = models.CharField(max_length=50)
    course_tutor_lname = models.CharField(max_length=50)
    course_date_start = models.DateTimeField(max_length=50)
    course_duration = models.FloatField()
    course_payment = models.PositiveIntegerField()
    belongs_to_category = models.ForeignKey(to=CourseCategory, on_delete=models.PROTECT, related_name='category_set')

    def __str__(self):
        return self.course_name


class StudentsEnrollsToCourses(models.Model):
    stud = models.ForeignKey(to=Students, on_delete=models.CASCADE, related_name='student_set')
    date_enrolled = models.DateTimeField(auto_now_add=50, blank=True, editable= True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, editable=True)
    enrolls_to_courses = models.ManyToManyField(to=Courses)

    def __str__(self):
        return self.enrolls_to_courses