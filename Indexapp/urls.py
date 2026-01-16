from django.urls import path
from . import views


urlpatterns = [
    path('index/',views.index,name='index'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('career/',views.career,name='career'),
]