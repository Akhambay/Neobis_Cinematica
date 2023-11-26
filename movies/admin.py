from django.contrib import admin
from .models import MovieTheatre, Movies, ShowTimes, Room

admin.site.register(MovieTheatre)
admin.site.register(Movies)
admin.site.register(ShowTimes)
admin.site.register(Room)
# admin.site.register(Seat)
