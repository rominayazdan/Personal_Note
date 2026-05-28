from urllib import request

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework import generics
from user.models import User

from user.serializers import RegisterUserSerializer, UserSerializer

class RegisterUserAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.validated_data['password'])
            user.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"result" : {"user_id" : user.id}})

class ViewUserAPI(generics.ListAPIView):
    #permission_classes = [IsAuthenticated]
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


    def get_queryset(self):

        queryset = User.objects.all()
        return queryset

class EditUserAPI(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    lookup_field = 'username'


    def get_queryset(self):
        user = self.request.user
        queryset = User.objects.filter()
        return queryset


class DeleteUserAPI(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    lookup_field = 'username'


    def get_queryset(self):
        user = self.request.user
        queryset = User.objects.filter()

        return queryset









