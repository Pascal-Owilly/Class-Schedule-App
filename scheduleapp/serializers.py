from rest_framework import serializers
from .models import Announcements, Comments, Session

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
        


