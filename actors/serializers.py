from actors.models import Actor
from rest_framework.serializers import ModelSerializer


class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'