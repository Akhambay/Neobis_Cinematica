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


class Movies(models.Model):
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
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}: {self.title} - {self.genre}"

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class Room(models.Model):
    room_choice = (
        ('IMAX 3D', 'IMAX 3D'),
        ('Standard', 'Standard'),
        ('Dolby Atmos', 'Dolby Atmos'),
    )

    cinema = models.ForeignKey(MovieTheatre, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=15, choices=room_choice)
    seat_id = models.ManyToOneRel

    def __str__(self):
        return f"{self.id}: {self.cinema} - {self.room_type}"

    class Meta:
        verbose_name = "Зал"
        verbose_name_plural = "Залы"


class ShowTimes(models.Model):
    start_session = models.TimeField()
    end_session = models.TimeField()
    cinema = models.ForeignKey(MovieTheatre, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.id}: {self.cinema} - {self.movie} | {self.start_session} - {self.price} KZT"

    class Meta:
        verbose_name = "Сеанс"
        verbose_name_plural = "Сеансы"


class Seat(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    row_number = models.PositiveIntegerField()
    seat_number = models.PositiveIntegerField()
    is_reserved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.row_number} ряд, {self.seat_number} место'

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"
