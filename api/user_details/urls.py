from django.urls import path
from .views import UserView, home



urlpatterns = [
    path('user_details', UserView.as_view()),
    path('Collinsoma', home)
]
