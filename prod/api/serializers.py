from api.models import Room, Roommate, User
from rest_framework import serializers


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class RoommateSerializer(serializers.ModelSerializer):
    room_password = serializers.CharField(write_only=True)

    class Meta:
        model = Roommate
        fields = "__all__"

    def create(self, validated_data):
        validated_data.pop("room_password", None)
        return super().create(validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
