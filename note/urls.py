from django.urls import path
from note.views import *




urlpatterns = [

    path('notes/', AddNoteAPI.as_view()),
    path('add-note/', AddNoteAPI.as_view()),
    path('', AddNoteAPI.as_view()),
    path('view-note/', ViewNoteAPI.as_view()),
    path('edit-note/<str:title>/', EditNoteAPI.as_view()),
    path('delete-note/<str:title>/', DeleteNoteAPI.as_view()),

]