from django.conf import settings
from django.db import models


class MovieTheatre(models.Model):
    title = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=50)
    building = models.PositiveIntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.title} - {self.city}"

    class Meta:
        verbose_name = "Кинотеатр"
        verbose_name_plural = "Кинотеатры"


class Movie(models.Model):
    genre_choice = (
        ('comedy', 'comedy'),
        ('animation', 'animation'),
        ('horror', 'horror'),
        ('drama', 'drama'),
        ('sci-fi', 'sci-fi'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    director = models.CharField(max_length=60)
    genre = models.CharField(max_length=10, choices=genre_choice)
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return f"{self.id}: {self.title} - {self.genre}"

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class ShowTimes(models.Model):
    start_session = models.TimeField()
    end_session = models.TimeField()
    cinema = models.ForeignKey(MovieTheatre, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # rooms = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}: {self.cinema} - {self.movie} | {self.start_session} - {self.end_session}"

    class Meta:
        verbose_name = "Сеанс"
        verbose_name_plural = "Сеансы"
