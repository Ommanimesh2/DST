from rest_framework import serializers
from .models import Rent


class JobCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Renting
        fields = '__all__'
