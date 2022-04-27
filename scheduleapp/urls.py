from django.urls import include, path
from rest_framework import routers
from .views import AnnouncementsList
from . import views

router = routers.DefaultRouter()
router.register(r'announcements', AnnouncementsList)

# urlpatterns = router.urls

urlpatterns = [
    path('api/', include(router.urls)),
    
]