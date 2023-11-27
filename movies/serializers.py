from rest_framework.serializers import ModelSerializer
from .models import MovieTheatre, Movies, ShowTimes, Room, Ticket, Seat, Feedback, PurchaseHistory


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


class RoomSerializers(ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'room_type']


class SeatSerializers(ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id', 'row_number', 'seat_number']


class TicketSerializers(ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'user', 'showtime', 'seat',
                  'quantity', 'payment_method', 'total_amount']


class FeedbackSerializers(ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'user', 'feedback']


class PurchaseHistorySerializers(ModelSerializer):
    class Meta:
        model = PurchaseHistory
        fields = ['id', 'user', 'purchase_date', 'total_amount']
