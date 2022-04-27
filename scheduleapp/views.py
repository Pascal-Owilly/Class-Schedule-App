from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AnnouncementSeializers, CommentsSerializer, SessionSerializer
from .models import Announcements, Comments, Session

# Create your views here.
class AnnouncementsList(viewsets.ModelViewSet):
    serializer_class = AnnouncementSeializers
    queryset = Announcements.objects.all()


# class CommentList(viewsets.ModelViewSet):
#     serializer_class = CommentsSerializer
#     queryset = Comments.objects.all()
    

class CommentList(APIView):
    def get(self, request, format=None):
        all_comments= Comments.objects.all()
        serializers = CommentsSerializer(all_comments, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = CommentsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
class Sessions(APIView):
    def get(self, request, *args, **kwargs):
        session = Session.objects.all()
        serializer = SessionSerializer(session, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



