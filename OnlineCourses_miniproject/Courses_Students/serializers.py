from rest_framework import serializers
from .models import Students, Courses, StudentsEnrollsToCourses, CourseCategory

# serializers.ModelSerializer
# Django easy to use -  common use case serializer.
# offers to us to create new, to add or alter the fields relevant to our models and to create new models.


class StudentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Students
        fields = ('url', 'first_name', 'last_name', 'email', 'occupation')


class CoursesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Courses
        fields = ('url', 'course_name', 'course_tutor_fname', 'course_tutor_lname',
                  'course_date_start', 'course_duration', 'course_payment','belongs_to_category')


class StudentsEnrollsToCoursesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentsEnrollsToCourses
        fields = ('url', 'stud', 'date_enrolled', 'updated_date', 'enrolls_to_courses')
    # TODO
    # def create_subscription(self, ** enrollment_data):
    #     choices = enrollment_data.pop('choice')
    #     return "User subscripted in course." + StudentsEnrollsToCourses.objects.create(**choice)
    #
    # def update_subscription(self):
    #     pass
    # def delete_subscription(self, choices):
    #     pass


class CourseCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ('url', 'category_name')