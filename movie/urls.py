from django.urls import path
#from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.urls import path



urlpatterns = [
    path('movies/all/', MixinMovieList.as_view()),
    path('movies/all/<int:pk>/', MixinMovieDetail.as_view()),

    path('add/', AddMovie.as_view()),    

    path('mycollection/', MyMoviesList.as_view()),
    path('mycollection/<int:pk>/', MyMovieDetail.as_view()),
    path('watched/', Watched.as_view()),
    path('watchlist/', Watchinglist.as_view()),

    


    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

   


]

#urlpatterns = format_suffix_patterns(urlpatterns)


