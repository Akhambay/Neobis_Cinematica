from django.conf import settings
from django.db import models
from accounts.models import CustomUser as User
import decimal


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
        return f"{self.title} - {self.genre}"

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class Room(models.Model):
    room_choice = (
        ('IMAX 3D', 'IMAX 3D'),
        ('Standard', 'Standard'),
        ('Dolby Atmos', 'Dolby Atmos'),
    )

    # cinema = models.ForeignKey(MovieTheatre, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=15, choices=room_choice)

    def __str__(self):
        return f"{self.room_type}"

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
        return f"{self.start_session} - {self.price} KZT"

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


class Ticket(models.Model):
    payment_choice = (
        ('debit card', 'debit card'),
        ('cash', 'cash'),
        ('Kaspi QR', 'Kaspi QR'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cinema = models.ForeignKey(MovieTheatre, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    showtime = models.ForeignKey(ShowTimes, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=15, choices=payment_choice)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_amount = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)

    def __str__(self):
        return f'Ticket ID: {self.id}'

    def save(self, *args, **kwargs):
        self.total_amount = self.showtime.price * self.quantity
        if self.payment_method == 'debit card':
            discount = decimal.Decimal('0.03')
            self.total_amount = decimal.Decimal(
                self.total_amount) * (1 - discount)
        super().save(*args, **kwargs)


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.TextField(max_length=200)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Feedback author: {self.user.username}'

    class Meta:
        ordering = ['-posted_at']
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратные связи"
