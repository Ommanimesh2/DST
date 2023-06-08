from rest_framework import serializers
from .models import Renting,Orders,query,FourImages,KVKs

class KVKSerializer(serializers.ModelSerializer):
    class Meta:
        model=KVKs
        fields='__all__'

class RentingSerializer(serializers.ModelSerializer):
    KVK = KVKSerializer()
    class Meta:
        model = Renting
        fields = '__all__'

    def create(self, validated_data):
        kvk_data = validated_data.pop('KVK')
        kvk = KVKs.objects.create(**kvk_data)
        renting = Renting.objects.create(KVK=kvk, **validated_data)
        return renting
    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = query
        fields = '__all__'

class FourImgSerializer(serializers.ModelSerializer):
    class Meta:
        model= FourImages
        fields='__all__'

