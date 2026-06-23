from reviews.models import Review
from reviews.serializers import ReviewSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
