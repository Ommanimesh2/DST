from rest_framework import serializers
from .models import Jobs


class JobCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Re
        fields = '__all__'
