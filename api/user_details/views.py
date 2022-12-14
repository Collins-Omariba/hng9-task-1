from wsgiref import headers
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserSerializer
from .models import User
from django.http import JsonResponse



class UserView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        List all the user details for given requested
        '''
        user_details = User.objects.all()
        serializer = UserSerializer(user_details, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def post(self, request, *args, **kwargs):
        data = {
            'slackUsername': request.data.get('slackUsername'), 
            'backend': request.data.get('backend'), 
            'age': request.data.get('age'),
            'bio': request.data.get('bio'),
        }
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def home(request, *args, **kwargs):
    header = {"Access-Control-Allow-Origin":"*"}
    data = {
        "slackUsername":"Collinsoma",
        "backend":True,
        "age":20,
        "bio":"Am a motivated django dev"
    }

    return JsonResponse(data, headers=header)