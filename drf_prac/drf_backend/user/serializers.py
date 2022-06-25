from rest_framework import serializers
from .models import User as UserModel

class UserSerializer(serializers.ModelSerializer):

    def validate(self, data):
    
        # try:
        #     http_method = self.context.get("request",{}).method
        # except:
        #     http_method = ""

        # if http_method == "POST":
        #     if data.get("email",'').split("@")[-1] not in VALID_EMAIL_LIST:
        #         raise serializers.ValidationError(
        #             detail={"error": "네이버 이메일,구글 이메일만 가입 할 수 있습니다."}
        #         )

        return data
    
    def create(self, validated_data):
        print("validated_data : ", validated_data)
        password = validated_data.pop("password", "")
        user = UserModel(**validated_data) 
        user.set_password(password)
        user.save()

        return user

    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email' , 'fullname', 'password']