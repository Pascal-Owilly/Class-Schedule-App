
from django.http import Http404, JsonResponse, request
from rest_framework import generics, permissions, status,viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from users.models import *
from .serializers import *
from rest_framework.generics import get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from .permissions import IsTmUser, IsStudentUser
from rest_framework.parsers import MultiPartParser, FormParser

class TmSignupView(generics.GenericAPIView):
    serializer_class=TmSignupSerializer

    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message":"account created successfully"
        })


class StudentSignupView(generics.GenericAPIView):
    serializer_class=StudentSignupSerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message":"account created successfully"
        })

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token, created=Token.objects.get_or_create(user=user)
        return Response({
            'token':token.key,
            'user_id':user.pk,
            'is_student':user.is_student,
            'is_tm':user.is_tm
        })


class LogoutView(APIView):
    def post(self, request, format=None):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)


class StudentOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsStudentUser]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user

class TmOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsTmUser]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user


# Create your views here.
class AnnouncementsList(viewsets.ModelViewSet):
    serializer_class = AnnouncementSerializers
    queryset = Announcements.objects.all()
    

class CommentList(APIView):
    def get(self, request, format=None):
        all_comments= Comments.objects.all()
        serializers = CommentsSerializer(all_comments, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = CommentsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class SingleComment(APIView):
    def get_comment(self, pk):
        try:
            return Comments.objects.get(pk=pk)
        except Comments.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        comments = self.get_comment(pk)
        serializer = CommentsSerializer(comments)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        comments = self.get_comment(pk)
        serializers = CommentsSerializer(comments, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        comments = self.get_comment(pk)
        comments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, safe=False)

        



class Sessions(APIView):
    def get(self, request, *args, **kwargs):
        session = Session.objects.all()
        serializer = SessionSerializer(session, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

    def post(self, request, format=None):
        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

class SingleSession(APIView):
    def get_session(self, pk):
        try:
            return Session.objects.get(pk=pk)
        except Session.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        session = self.get_session(pk)
        serializer = SessionSerializer(session)
        return JsonResponse(serializer.data)

    def put(self, request, pk, format=None):
        session = self.get_session(pk)
        serializers = SessionSerializer(session, request.data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data, safe=False)
        else:
            return JsonResponse(serializers.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

    def delete(self, request, pk, format=None):
        session = self.get_session(pk)
        session.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)


class Students(APIView):
    
    def get(self, request, format=None):
        all_students= Student.objects.all()
        serializers = StudentSerializer(all_students, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = StudentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class Attendance(APIView):
    def get_attendance(self, id):
        try:
            return Attendance.objects.get(id=id)
        except Attendance.DoesNotExist:
            return Http404

    def get(self, request, id, format=None):
        attendance = self.get_attendance(id)
        serializer = AttendanceSerializer(attendance)
        return JsonResponse(serializer.data)

    def put(self, request, id, format=None):
        attendance = self.get_attendance(id)
        serializers = AttendanceSerializer(attendance, request.data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data, safe=False)
        else:
            return JsonResponse(serializers.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)
 


class Courses(APIView):
    
    def get(self, request, format=None):
        all_courses= Course.objects.all()
        serializers = CourseSerializer(all_courses, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = CourseSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class GetUser(APIView):  
    def get(self,request,id):
        print(id)
        if id:
            user = get_object_or_404(User, id=id)

        
            User_serializer = UserSerializer(user) 
        
            return Response(User_serializer.data)





