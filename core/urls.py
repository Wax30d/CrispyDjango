# crispy/urls.py
from django.urls import path
from core import views
# Add this

urlpatterns = [
    path('', views.signup, name='signup'),
    path('crispy/', views.crispy_signup, name='crispy_signup'),
]
