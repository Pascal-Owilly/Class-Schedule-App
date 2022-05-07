from django.urls import path
from .views import ( CustomAuthToken, LogoutView, StudentOnlyView, StudentSignupView, TmOnlyView, TmSignupView)

urlpatterns=[
    path('signup/tm/', TmSignupView.as_view()),
    path('signup/student/', StudentSignupView.as_view()),
    path('login/', CustomAuthToken.as_view(), name='auth-token'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
    path('tm/dashboard/', TmOnlyView.as_view(), name='tmdashboard'),
    path('student/dashboard/', StudentOnlyView.as_view(), name='studentdashboard'),
]