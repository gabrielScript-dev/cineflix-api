from django.urls import path
from movies.views import MovieListCreateAPIView, MovieRetrieveUpdateDestroyAPIView


urlpatterns = [
    path(route='movies/', view=MovieListCreateAPIView.as_view(), name='movies-create-list'),
    path(route='movies/<int:pk>', view=MovieRetrieveUpdateDestroyAPIView.as_view(), name='movies-detail-view')
]
