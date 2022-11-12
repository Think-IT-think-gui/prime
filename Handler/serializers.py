from rest_framework import serializers
from . models import Login_info,User_info,Posts_info,Hype_info,User_comments,User_follower,User_messeges,User_List,Message_Api

class ClientLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login_info
        fields = '__all__'

class ClientInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_info
        fields = '__all__'

class ClientPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts_info
        fields = '__all__'

class ClientHypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hype_info
        fields = '__all__'  

class ClientCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_comments
        fields = '__all__'  



class ClientFollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_follower
        fields = '__all__'  

class ClientMessegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_messeges
        fields = '__all__'          


class ClientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_List
        fields = '__all__'   

class ClientChatapiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message_Api
        fields = '__all__'  

        