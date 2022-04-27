from pyexpat import model
from rest_framework import serializers
from .models import Announcements

class AnnouncementSeializers(serializers.ModelSerializer):
    class Meta:
        model = Announcements
        fields = '__all__'
        



