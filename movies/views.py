from rest_framework import generics
from rest_framework import viewsets
from .models import MovieTheatre, Movies, ShowTimes, Ticket, Feedback, PurchaseHistory
from .serializers import (MovieTheatreSerializers, MoviesSerializers, ShowTimesSerializers,
                          TicketSerializers, FeedbackSerializers, PurchaseHistorySerializers)


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


class FeedbacksList(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializers


class FeedbacksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializers


class PurchaseHistoryList(generics.ListCreateAPIView):
    queryset = PurchaseHistory.objects.all()
    serializer_class = PurchaseHistorySerializers


class PurchaseHistoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseHistory.objects.all()
    serializer_class = PurchaseHistorySerializers
