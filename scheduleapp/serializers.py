from rest_framework import serializers
from .models import Announcements, Comments

class AnnouncementSeializers(serializers.ModelSerializer):
    class Meta:
        model = Announcements
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'




