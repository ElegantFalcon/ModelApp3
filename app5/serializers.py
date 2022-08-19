from rest_framework import serializers
from app5.models import UserData

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData  
        fields = ('username' , 'phone_no' , 'dob' , 'email', 'pswd')
