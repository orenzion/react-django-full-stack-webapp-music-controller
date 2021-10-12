from django.urls import path
from .views import RoomView

urlpatterns = [
    # take the 'RoomView' class and return it as a view to the 'api/home' path
    path('room', RoomView.as_view()),

]
