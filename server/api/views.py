from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from api.serializers import UserSerializer
from rest_framework import permissions
# from api.permissions import IsOwnerOrReadOnly
from rest_framework.authtoken.models import Token
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from django.http import Http404

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

from django.contrib.auth import get_user_model
User = get_user_model()

import boto3

class UserList(generics.ListAPIView):
    """Get list of user or create one

    get:
    Return a list of all the existing users.

    post:
    Create a new user instance.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=HTTP_404_NOT_FOUND)


# class UserPicture(APIView):

    # model = User
    # fields = ['upload', ]

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     user = User.objects.all()
    #     context['user'] = user
    #     return context

        
    # def put(self, request, pk):
    #     # print(pk)
    #     file = request.data.get("file")
    #     print(file)
    #     if file is not None:
            
    #         client = boto3.resource(
    #             's3',
    #             # I would not hard code this in real project...
    #             aws_access_key_id='AKIAI2NK57GGZPQY6KMQ',
    #             aws_secret_access_key='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',
    #         )

    #         # Print out bucket names for testing purpose
    #         for bucket in client.buckets.all():
    #             print(bucket.name)

    #     return Response({"ok"}, status=HTTP_200_OK)

class AuthLogin(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        if email is None or password is None:
            return Response({'error': 'Please provide both email and password'},
                            status=HTTP_400_BAD_REQUEST)

        user = User.objects.get(email=email)
        if not user.check_password(password):
            return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)

        token, _ = Token.objects.get_or_create(user=user)
        user = UserSerializer(user)
        return Response({
            'token': token.key,
            'user': user.data
        }, status=HTTP_200_OK)

class AuthRegister(APIView):
    def post(self, request):
        email = request.data.get("email")
        name = request.data.get("name")
        password = request.data.get("password")
        passwordConfirmation = request.data.get("passwordConfirmation")

        if email is None or name is None or password is None:
            return Response({'error': 'Please provide all required fields'},
                            status=HTTP_400_BAD_REQUEST)
        
        if password != passwordConfirmation:
            return Response({'error': 'Password and passwordCOnfirmation don\'t match'},
                            status=HTTP_400_BAD_REQUEST)
        
        # create fields by fields to not save unnecessary fields (username)
        user = User.objects.create(email=email, name=name, password=make_password(password))

        token, _ = Token.objects.get_or_create(user=user)
        user = UserSerializer(user)
        return Response({
            'token': token.key,
            'user': user.data
        }, status=HTTP_200_OK)
