from dataclasses import fields
from rest_framework import serializers

from scheduleapp.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name','email', 'is_student','password']
        extra_kwargs={
            'password':{'write_only':True}
        }
    
    def save(self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name']
        )
        password=self.validated_data['password']
        user.set_password(password)
        user.is_student=True
        user.save()
        Student.objects.create(user=user)
        return user


class AnnouncementSerializers(serializers.ModelSerializer):
    comments = serializers.StringRelatedField(many=True)

    class Meta:
        model = Announcements
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

# class SessionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Session
#         fields = '__all__'


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

