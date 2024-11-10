from api.models import Room, Roommate
from rest_framework import serializers


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class RoommateSerializer(serializers.ModelSerializer):
    user_password = serializers.CharField(write_only=True)

    class Meta:
        model = Roommate
        fields = "__all__"

    def create(self, validated_data):
        validated_data.pop("user_password", None)
        return super().create(validated_data)
