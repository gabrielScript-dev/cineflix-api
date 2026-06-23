from django.urls import path
from genres.views import GenreListCreateAPIView, GenreRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('genres/', view=GenreListCreateAPIView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>', view=GenreRetrieveUpdateDestroyAPIView.as_view(), name='genre-detail-view')
]