from django.urls import path
from teachers import views

urlpatterns = [
    path('name/', views.home, name='home'),
]