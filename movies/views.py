from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MovieTheatre, Movies, ShowTimes, Ticket
from .serializers import MovieTheatreSerializers, MoviesSerializers, ShowTimesSerializers, TicketSerializers, SeatSerializers


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


class TicketsList(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializers


class TicketsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializers


@api_view(['POST'])
def calculate_total_price(request):
    data = request.data
    showtime_id = data.get('showtime_id', [])
    quantities = data.get('quantities', [])

    total_price = 0

    for showtime_id, quantity in zip(showtime_id, quantities):
        try:
            showtime = ShowTimes.objects.get(pk=showtime_id)
            total_price += showtime.price * quantity
        except ShowTimes.DoesNotExist:
            return Response({'error': f'Showtime with id {showtime_id} not found'}, status=404)

    return Response({'total_price': total_price})
