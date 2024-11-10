from api import views
from django.urls import path


urlpatterns = [
    path("room", views.RoomAPIListCreateView.as_view()),
    path("room/connect", views.RoommateAPICreateView.as_view()),
    path("room/<int:pk>", views.RoomAPIRetrieveView.as_view()),
    path("user/create", views.UserAPICreateView.as_view()),
    path("user/<int:user_id>/rooms", views.UserRoomsAPIView.as_view()),
    path("roommate/<int:pk>", views.RoommateAPIRetrieveUpdateDestroyView.as_view()),
    path("rooms/<int:room_id>/users/", views.RoommateView.as_view()),
]
