from .models import WatchList, Movie
from .serializers import *
from .serializers import UserSerializer, RegisterSerializer

from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as django_login, logout as django_logout

from django.http import Http404, HttpResponse


class MixinMovieList(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    
class MixinMovieDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    



 ### User Movie 
 
class MyMoviesList(LoginRequiredMixin, APIView):
    login_url = '/login/'
    redirect_field_name = 'login'
    model = WatchList
    """
    List all instance, or create a new instance.
    """
    def get(self, request, format=None):
        instance = WatchList.objects.filter(user = request.user)
        serializer = WatchListSerializer(instance, many=True)
        return Response(serializer.data)





class Watched(LoginRequiredMixin,APIView):
    login_url = '/login/'
    redirect_field_name = 'login'
    model = WatchList
    """
    List all instance, or create a new instance.
    """
    def get(self, request, format=None):
        instance = WatchList.objects.filter(user = request.user, watch_info='Already Watched')
        serializer = WatchListSerializer(instance, many=True)
        return Response(serializer.data)

        
class Watchinglist(LoginRequiredMixin,APIView):
    login_url = '/login/'
    redirect_field_name = 'login'
    model = WatchList
    """
    List all instance, or create a new instance.
    """
    def get(self, request, format=None):
        instance = WatchList.objects.filter(user = request.user, watch_info='Add to Watch List')
        serializer = WatchListSerializer(instance, many=True)
        return Response(serializer.data)



    
######    adding movies watch status   ##########

from rest_framework import generics
from .serializers import AddSerializer

class AddMovie(LoginRequiredMixin,generics.CreateAPIView):
    login_url = '/login/'
    redirect_field_name = 'login'
    model = WatchList
    queryset = WatchList.objects.all()
    serializer_class = AddSerializer

    user_field = 'user'
    def get_user_field(self):
        return self.user_field


    def perform_create(self, serializer):
        kwargs = {
                   self.get_user_field(): self.request.user
                  }
        serializer.save(**kwargs)


class MyMovieDetail(LoginRequiredMixin,generics.RetrieveUpdateDestroyAPIView):
    login_url = '/login/'
    redirect_field_name = 'login'
    model = WatchList
    queryset = WatchList.objects.all()
    serializer_class = UpdateSerializer


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        })

class LoginView(generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        return Response(status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return Response(status=204)