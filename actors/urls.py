from django.urls import path
from actors.views import ActorListCreateAPIView, ActorRetrieveUpdateDestroyAPIView

urlpatterns = [
    path(route='actors/', view=ActorListCreateAPIView.as_view(), name='actor-create-list'),
    path(route='actors/<int:pk>', view=ActorRetrieveUpdateDestroyAPIView.as_view(), name='actor-detail-view')
]