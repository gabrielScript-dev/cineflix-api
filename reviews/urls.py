from django.urls import path
from reviews.views import ReviewListCreateAPIView, ReviewRetrieveUpdateDestroyAPIView


urlpatterns = [
    path(route='reviews/', view=ReviewListCreateAPIView.as_view(), name='review-create-list'),
    path(route='reviews/<int:pk>', view=ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review-detail-view')
]
