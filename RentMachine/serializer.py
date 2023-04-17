from rest_framework import serializers
from .models import Renting,Orders


class RentingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Renting
        fields = '__all__'
    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'