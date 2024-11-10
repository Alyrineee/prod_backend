from api.models import Room, Roommate
from api.permissions import IsRoomAdmin
from api.serializers import RoommateSerializer, RoomSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView


class RoomAPIListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoommateAPICreateView(generics.CreateAPIView):
    queryset = Roommate.objects.all()
    serializer_class = RoommateSerializer
    permission_classes = (IsRoomAdmin,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data.get("user_password", None)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class RoommateAPIRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Roommate.objects.all()
    serializer_class = RoommateSerializer


class RoommateView(APIView):
    def get(self, request, room_id):
        room_users = Roommate.objects.filter(room_id=room_id)
        serializer = RoommateSerializer(room_users, many=True)
        return Response(serializer.data)
