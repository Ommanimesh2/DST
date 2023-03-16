from rest_framework import serializers
from .models import Stalls


class StallsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stalls
        fields = '__all__'
