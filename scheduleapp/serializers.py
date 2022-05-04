from rest_framework import serializers
from .models import Announcements, Comments, Session,Profile,Course,Attendance, Student,Tm
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4)
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)


    class Meta:
        model =User
        fields =['username','password', 'email', 'first_name', 'last_name']

    
    def validate(self,attrs):
        email=attrs.get('email','')
        if User.objects.filter(email= email).exists():
            raise serializers.ValidationError({'email': ('Email is already in use')})
        return super().validate(attrs)
    
    def create(self, validate_data):
        return User.objects.create_user(**validate_data)

class AnnouncementSerializers(serializers.ModelSerializer):
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

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    username = serializers.CharField(max_length=80, min_length=2)

    class Meta:
        model = User
        fields =['username', 'password']


