from rest_framework import serializers
from .models import WatchList, Movie
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import exceptions


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', )

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
    


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        #exclude = ['id']
        fields = '__all__'

class WatchListSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = WatchList
        fields = ['id', 'user', 'movie', 'watch_info']


class UpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchList
        fields = ['watch_info']        

        
class AddSerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchList
        fields = [ 'movie', 'watch_info']        


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "User is deactivated."
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to login with given credentials."
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide username and password both."
            raise exceptions.ValidationError(msg)
        return data
              
        

        


