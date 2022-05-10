from django.urls import include, path, re_path
from . import views
from .views import ( CustomAuthToken, LogoutView, ReigsterView)
from rest_framework import routers
from .views import AnnouncementsList

router = routers.DefaultRouter()
router.register(r'announcements', AnnouncementsList)

urlpatterns=[
    path('api/', include(router.urls)),
    path('adduser/', ReigsterView.as_view()),
    path('login/', CustomAuthToken.as_view(), name='auth-token'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
    path('comments/', views.CommentList.as_view()),
    re_path(r'api/comments/(?P<pk>[0-9]+)/$',views.SingleComment.as_view()),
    path('students/', views.Students.as_view()),
    path('courses/', views.Courses.as_view()),
    path('attendance/<int:id>', views.Attendance.as_view()),
]

