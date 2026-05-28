from django.urls import path
from user.views import *





urlpatterns = [
    path('signup', RegisterUserAPI.as_view()),
    path('view-users', ViewUserAPI.as_view()),
    path('edit-user/<str:username>/', EditUserAPI.as_view()),
    path('delete-user/<str:username>/', DeleteUserAPI.as_view()),

]
