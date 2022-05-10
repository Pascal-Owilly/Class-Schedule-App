from dataclasses import fields
from rest_framework import serializers

from users.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'email', 'is_student', 'is_tm']

class TmSignupSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"}, write_only=True)
    class Meta:
        model=User
        fields=['username','email','password', 'password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
    
    def save(self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"error":"password do not match"})
        user.set_password(password)
        user.is_tm=True
        user.save()
        Tm.objects.create(user=user)
        return user


class StudentSignupSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"}, write_only=True)
    class Meta:
        model=User
        fields=['username','email','password', 'password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
    

    def save(self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"error":"password do not match"})
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

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
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






















