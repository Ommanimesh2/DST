from rest_framework import serializers
from .models import Renting


class JobCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Renting
        fields = '__all__'
