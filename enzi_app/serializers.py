from rest_framework import serializers
from enzi_app.models import ClientBooking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientBooking
        fields = ('__all__')