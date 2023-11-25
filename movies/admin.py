from django.contrib import admin
from .models import MovieTheatre, Movie, ShowTimes

admin.site.register(MovieTheatre)
admin.site.register(Movie)
admin.site.register(ShowTimes)
