from django.urls import include, path
from rest_framework import routers
from .views import AnnouncementsList, CommentList
from . import views

router = routers.DefaultRouter()
router.register(r'announcements', AnnouncementsList)
# router.register(r'comment', CommentList)


# urlpatterns = router.urls

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/comments/', views.CommentList.as_view()),
    path('api/sessions/', views.Sessions.as_view()),
]