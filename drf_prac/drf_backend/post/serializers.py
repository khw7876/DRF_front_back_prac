from rest_framework import serializers
from .models import Post as PostModel
from user.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = PostModel
        fields = ['id', 'user', 'title','content']