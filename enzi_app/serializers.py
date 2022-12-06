from rest_framework import serializers
from enzi_app.models import ClientBooking, MpesaResponse


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientBooking
        fields = ('__all__')

class MpesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MpesaResponse 
        fields = ('__all__')