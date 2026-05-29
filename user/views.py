from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status

from user.serializers import RegisterUserSerializer






class RegisterUserAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                data = {'result':{'user_id' : user.id, 'username' : user.username}},
                status = status.HTTP_201_CREATED,
            )
        else:
            return Response(
                data = {'Error': serializer.errors},
                status = status.HTTP_400_BAD_REQUEST,
            )




