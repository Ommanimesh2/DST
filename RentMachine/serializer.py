from rest_framework import serializers
from .models import Renting


class RentingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Renting
        fields = '__all__'
