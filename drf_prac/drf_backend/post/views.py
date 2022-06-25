from functools import partial
from os import stat
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

from post.serializers import PostSerializer
from post.models import Post as PostModel

class PostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        user = request.user
        post_obj = PostModel.objects.filter(user = user)
        return Response(PostSerializer(post_obj, many = True).data, status = status.HTTP_200_OK)

    def post(self,request):
        user = request.user
        request.data['user'] = user
        post_serializer = PostSerializer(data = request.data)
        if post_serializer.is_valid():
            post_serializer.save(user=user)
            return Response(post_serializer.data, status = status.HTTP_200_OK)
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request, post_id):
        post_obj = PostModel.objects.get(id = post_id)
        post_serializer = PostSerializer(post_obj, data=request.data, partial=True)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_200_OK)
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request):
        return Response()

# Create your views here.

