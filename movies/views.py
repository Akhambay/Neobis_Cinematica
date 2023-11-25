from rest_framework import generics
from .models import MovieTheatre, Movies, ShowTimes
from .serializers import MovieTheatreSerializers, MoviesSerializers, ShowTimesSerializers


class MovieTheatreList(generics.ListCreateAPIView):
    queryset = MovieTheatre.objects.all()
    serializer_class = MovieTheatreSerializers


class MovieTheatreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieTheatre.objects.all()
    serializer_class = MovieTheatreSerializers


class MoviesList(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializers


class MoviesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializers


class ShowTimesList(generics.ListCreateAPIView):
    queryset = ShowTimes.objects.all()
    serializer_class = ShowTimesSerializers


class ShowTimesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShowTimes.objects.all()
    serializer_class = ShowTimesSerializers
