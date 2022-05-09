from django.urls import include, path, re_path
from rest_framework import routers
from .views import AnnouncementsList, CommentList
from . import views
from .views import (CustomAuthToken,LogoutView,ReigsterView,LoginView)


router = routers.DefaultRouter()
router.register(r'announcements', AnnouncementsList)

urlpatterns = [
    path('api/', include(router.urls)),
    path('adduser/', ReigsterView.as_view()),
    path('comments/', views.CommentList.as_view()),
    re_path(r'api/comments/(?P<pk>[0-9]+)/$',views.SingleComment.as_view()),
    # path('sessions/', views.Sessions.as_view()),
    # re_path(r'api/sessions/(?P<pk>[0-9]+)/$', views.SingleSession.as_view()),
    path('students/', views.Students.as_view()),
    path('courses/', views.Courses.as_view()),
    path('attendance/<int:id>', views.Attendance.as_view()),
    # path('tm/dashboard/', TmOnlyView.as_view(), name='tmdashboard'),
    # path('student/dashboard/', StudentOnlyView.as_view(), name='studentdashboard'),
    path('profile/<int:id>/', views.Userprofile.as_view()),
    # path('login/', LoginView.as_view()),
    path('login/', CustomAuthToken.as_view(), name='auth-token'),
    path('getuser/<int:id>/', views.GetUser.as_view()),
]

