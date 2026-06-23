from movies.models import Movie
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.db.models import Avg


class MovieSerializer(ModelSerializer):

    rate = SerializerMethodField(read_only=True)

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return rate
        
        return None

    class Meta:
        model = Movie
        fields = '__all__'
