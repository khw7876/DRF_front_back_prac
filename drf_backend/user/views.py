from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from django.db.models import F, Q
from django.contrib.auth import authenticate, login, logout

from user.serializers import UserSerializer

from user.models import User as UserModel
# Create your views here.

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self,request):
        return({"message" : "get_response"})
            
    def post(self,request):
        user = authenticate(request, **request.data)

        if user:
            login(request,user)
            return Response({"message" : "login완료!"}, status = status.HTTP_200_OK)

        return Response({"message" : "아이디나 비밀번호가 일치하지 않습니다!!"}, status = status.HTTP_400_BAD_REQUEST)

        

    def put(self,request):
        return({"message" : "put_response"})

    def delete(self,request):
        logout(request)
        pass


class UserView(APIView):
    permissions_class = [permissions.AllowAny]

    def get(self, request):

        user_serializer = UserSerializer(data = request.date, conetxt = {"request" :request})

        return Response(user_serializer.data , status = status.status)
    
    def post(self, request):
        
        user_serializer = UserSerializer(data = request.data, context={"request":request})
        print("request.data",user_serializer)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data , status = status.HTTP_200_OK)
        
        return Response(user_serializer.errors , status=status.HTTP_400_BAD_REQUEST)


        
    
    def put(self, request):

        return Response({"message" : "put!!"})
        
    
    def delete(self, request):

        return Response({"message" : "delete!!"})
        

