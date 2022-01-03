from rest_framework import serializers
from .models import *

class HeaderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = '__all__'

class HeaderdisSerialzers(serializers.ModelSerializer):
    class Meta:
        model = Headerdis
        fields = '__all__'