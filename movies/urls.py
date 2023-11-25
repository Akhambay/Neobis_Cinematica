from django.urls import path
from . import views

urlpatterns = [
    path('movietheaters/', views.MovieTheatreList.as_view()),
    path('movietheaters/<int:pk>/', views.MovieTheatreDetail.as_view()),
    path('movies/', views.MoviesList.as_view()),
    path('movies/<int:pk>/', views.MoviesDetail.as_view()),
    path('showtimes/', views.ShowTimesList.as_view()),
    path('showtimes/<int:pk>/',
         views.ShowTimesDetail.as_view()),
]
