from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

from .serializers import AnnouncementSeializers, CommentsSerializer, SessionSerializer,ProfileSerializer,CourseSerializer,AttendanceSerializer,StudentSerializer
from .models import Announcements, Comments, Session, Student
from django.contrib.auth.models import User

# Create your views here.
class AnnouncementsList(viewsets.ModelViewSet):
    serializer_class = AnnouncementSeializers
    queryset = Announcements.objects.all()
    

class CommentList(APIView):
    def get(self, request, format=None):
        all_comments= Comments.objects.all()
        serializers = CommentsSerializer(all_comments, many=True)
        return JsonResponse(serializers.data, safe=False)
    
    def post(self, request, format=None):
        serializers = CommentsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data, safe=False, status=status.HTTP_201_CREATED)
        return JsonResponse(serializers.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

class SingleComment(APIView):
    def get_comment(self, pk):
        try:
            return Comments.objects.get(pk=pk)
        except Comments.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        comments = self.get_comment(pk)
        serializer = CommentsSerializer(comments)
        return JsonResponse(serializer.data, safe=False)

    def put(self, request, pk, format=None):
        comments = self.get_comment(pk)
        serializers = CommentsSerializer(comments, request.data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data, safe=False)
        else:
            return JsonResponse(serializers.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

    def delete(self, request, pk, format=None):
        comments = self.get_comment(pk)
        comments.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT, safe=False)

        



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
        return JsonResponse(serializers.data,  safe=False)
    
    def post(self, request, format=None):
        serializers = StudentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(serializers.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)


class Attendance(APIView):
    def get_attendance(self, pk):
        try:
            return Attendance.objects.get(pk=pk)
        except Attendance.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        attendance = self.get_attendance(pk)
        serializer = AttendanceSerializer(attendance)
        return JsonResponse(serializer.data)

    def put(self, request, pk, format=None):
        attendance = self.get_attendance(pk)
        serializers = AttendanceSerializer(attendance, request.data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data, safe=False)
        else:
            return JsonResponse(serializers.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)
    