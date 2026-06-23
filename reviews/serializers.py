from reviews.models import Review
from rest_framework.serializers import ModelSerializer, ValidationError


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate_stars(self, value):
        if value < 0 or value > 5:
            raise ValidationError('Avaliação precisa estar dentro do intervalo entre 0 e 5')
        
        return value
