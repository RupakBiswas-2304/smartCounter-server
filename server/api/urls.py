from django.urls import path
from .views import *

urlpatterns = [
    path('',Index.as_view()),
    path('count',Count.as_view()),
    path('register',Register.as_view()),
    path('login',Login.as_view()),
    path('rooms',Rooms.as_view()),
    path('devices',Devices.as_view())
]