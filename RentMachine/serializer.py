from rest_framework import serializers
from .models import Renting,Orders,query,FourImages,KVKs


class KVKSerializer(serializers.ModelSerializer):
    class Meta:
        model = KVKs
        fields = "__all__"

class RentingSerializer(serializers.ModelSerializer):
    KVK = KVKSerializer(read_only= True)  # Define the KVK field
    
    class Meta:
        model = Renting
        fields = "__all__"
        depth = 1
      
        def create(self, validated_data):
           kvk_id = validated_data.pop('KVK', None)
           if kvk_id:
            kvk = KVKs.objects.get(pk=kvk_id)
            validated_data['KVK'] = kvk
           return super().create(validated_data)
    
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

