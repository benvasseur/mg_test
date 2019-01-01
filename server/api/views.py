from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from api.serializers import UserSerializer
from rest_framework import permissions
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

from rest_framework.parsers import MultiPartParser
import boto3
import os


class UserList(generics.ListAPIView):
    """Get list of user or create one
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

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

class FileUploadView(APIView):
    """Upload profile picture to s3 and delete old one if exist
    """
    parser_classes = (MultiPartParser,)

    def put(self, request, pk):
        file_obj = request.FILES['file']
        user = User.objects.get(pk=pk)

        print(user)

        # S3 client init
        client = boto3.resource(
            's3',
            aws_access_key_id='AKIAI2NK57GGZPQY6KMQ',
            aws_secret_access_key='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',
        )

        if user.profile_picture != '':
            # Remove old file if exist
            old_key = user.profile_picture.replace('https://s3.ap-northeast-2.amazonaws.com/storage-mg/', '')
            client.Bucket('storage-mg').delete_objects(Delete={
                'Objects': [
                    {
                        'Key': old_key,
                    },
                ],
            },)

        # Upload new file to s3
        data = file_obj.read()
        filename, file_extension = os.path.splitext(file_obj.name)

        key = 'user/%s/%s%s'%(pk, filename, file_extension)
        client.Bucket('storage-mg').put_object(Key=key, Body=data)

        # Save image path to User
        user = User.objects.get(pk=pk)
        user.profile_picture = 'https://s3.ap-northeast-2.amazonaws.com/storage-mg/%s'%(key)
        user.save()
        user = UserSerializer(user)

        return Response(user.data, status=200)

class AuthLogin(APIView):
    """Authenticate user and return token and user data
    """
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        
        # Check required fields
        if email is None or password is None:
            return Response({'error': 'Please provide both email and password'},
                            status=HTTP_400_BAD_REQUEST)

        # Check if password match email
        user = User.objects.get(email=email)
        if not user.check_password(password):
            return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)

        # Generate token and return user object and token
        token, _ = Token.objects.get_or_create(user=user)
        user = UserSerializer(user)
        return Response({
            'token': token.key,
            'user': user.data
        }, status=HTTP_200_OK)

class AuthRegister(APIView):
    """Register and login user
    """
    def post(self, request):
        email = request.data.get("email")
        name = request.data.get("name")
        password = request.data.get("password")
        password_confirmation = request.data.get("passwordConfirmation")

        # Check fields
        if email is None or name is None or password is None:
            return Response({'error': 'Please provide all required fields'},
                            status=HTTP_400_BAD_REQUEST)

        if password != password_confirmation:
            return Response({'error': 'Password and passwordConfirmation don\'t match'},
                            status=HTTP_400_BAD_REQUEST)
        
        # create fields by fields to not save unnecessary fields (username)
        user = User.objects.create(email=email, name=name, password=make_password(password))

        # Generate token and return user object and token
        token, _ = Token.objects.get_or_create(user=user)
        user = UserSerializer(user)
        return Response({
            'token': token.key,
            'user': user.data
        }, status=HTTP_200_OK)
