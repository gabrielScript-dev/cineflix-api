from genres.models import Genre
from genres.serializers import GenreSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class GenreListCreateAPIView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

