from api import views
from django.urls import path


urlpatterns = [
    path("room", views.RoomAPIListCreateView.as_view()),
    path("roommates", views.RoommateAPICreateView.as_view()),
    path("roommate/<int:pk>", views.RoommateAPIRetrieveUpdateDestroyView.as_view()),
    path("rooms/<int:room_id>/users/", views.RoommateView.as_view()),
]
