from rest_framework import serializers

class Phone_serializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11)
