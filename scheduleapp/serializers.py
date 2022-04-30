from rest_framework import serializers
from .models import Announcements, Comments, Session,Profile,Course,Attendance, Student

class AnnouncementSeializers(serializers.ModelSerializer):
    class Meta:
        model = Announcements
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Profile
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'        

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
