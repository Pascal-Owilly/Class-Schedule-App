from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AnnouncementSeializers, CommentsSerializer
from .models import Announcements, Comments

# Create your views here.
class AnnouncementsList(viewsets.ModelViewSet):
    serializer_class = AnnouncementSeializers
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
            return Response(serializers.data, status=status.HTTP_201_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        

