from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('students/<int:id>/', views.detail, name='student-detail'),
]


