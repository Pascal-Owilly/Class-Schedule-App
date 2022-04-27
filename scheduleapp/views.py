from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AnnouncementSeializers
from .models import Announcements

# Create your views here.
class AnnouncementsList(viewsets.ModelViewSet):
    serializers_class = AnnouncementSeializers
    queryset = Announcements.objects.all()
    



