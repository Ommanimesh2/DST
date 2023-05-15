from rest_framework import serializers
from .models import Renting,Orders,query


class RentingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Renting
        fields = '__all__'
    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = query
        fields = '__all__'