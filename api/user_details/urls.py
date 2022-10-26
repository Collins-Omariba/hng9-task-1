from django.urls import path
from .views import UserView



urlpatterns = [
    path('user_details', UserView.as_view()),
]
