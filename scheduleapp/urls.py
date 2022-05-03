from django.urls import include, path, re_path
from rest_framework import routers
from .views import AnnouncementsList, CommentList
from . import views

router = routers.DefaultRouter()
router.register(r'announcements', AnnouncementsList)

urlpatterns = [
    path('api/', include(router.urls)),
    path('comments/', views.CommentList.as_view()),
    re_path(r'api/comments/(?P<pk>[0-9]+)/$',views.SingleComment.as_view()),
    path('sessions/', views.Sessions.as_view()),
    re_path(r'api/sessions/(?P<pk>[0-9]+)/$', views.SingleSession.as_view()),
    path('students/', views.Students.as_view()),
    path('attendance/<int:pk>', views.Attendance.as_view()),
]

