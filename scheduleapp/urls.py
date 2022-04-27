from django.urls import include, path
from rest_framework import routers
from .views import AnnouncementsList, CommentList
from . import views

router = routers.DefaultRouter()
router.register(r'announcements', AnnouncementsList)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/comments', views.CommentList.as_view()),
]