from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from note.serializers import NoteSerializer
from rest_framework.permissions import AllowAny
from user.permissions import *
from note.paginations import NotePagination

from note.models import Note


class AddNoteAPI(generics.ListCreateAPIView):
    #permission_classes = (AllowAny,)
    permission_classes = (UserPermissions,)

    serializer_class = NoteSerializer
    pagination_class = NotePagination

    def get_queryset(self):
        user = self.request.user
        queryset = Note.objects.filter(writer_id=user.id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)


class ViewNoteAPI(generics.ListAPIView):
    permission_classes = (UserPermissions,)
    serializer_class = NoteSerializer
    pagination_class = NotePagination
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        queryset = Note.objects.filter(writer_id=user.id)
        return queryset

class EditNoteAPI(generics.RetrieveUpdateAPIView):
    permission_classes = (UserPermissions,)
    serializer_class = NoteSerializer
    lookup_field = 'title'

    def get_queryset(self):
        user = self.request.user
        queryset = Note.objects.filter(writer_id=user.id)

        return queryset

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)

class DeleteNoteAPI(generics.DestroyAPIView):
    permission_classes = (UserPermissions,)

    serializer_class = NoteSerializer
    lookup_field = 'title'

    def get_queryset(self):
        user = self.request.user
        queryset = Note.objects.filter(writer_id=user.id)

        return queryset

