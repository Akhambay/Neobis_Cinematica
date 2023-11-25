from rest_framework.serializers import ModelSerializer
from .models import MovieTheatre, Movies, ShowTimes


class MovieTheatreSerializers(ModelSerializer):
    class Meta:
        model = MovieTheatre
        fields = ['id', 'title', 'city', 'street',
                  'building', 'start_time', 'end_time']


class MoviesSerializers(ModelSerializer):
    class Meta:
        model = Movies
        fields = ['id', 'title', 'description', 'director',
                  'genre', 'date_start', 'date_end']


class ShowTimesSerializers(ModelSerializer):
    class Meta:
        model = ShowTimes
        fields = ['id', 'start_session', 'end_session', 'cinema', 'movie']
