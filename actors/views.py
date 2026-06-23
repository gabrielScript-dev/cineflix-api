from actors.models import Actor
from actors.serializers import ActorSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ActorListCreateAPIView(ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer