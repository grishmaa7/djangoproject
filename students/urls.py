from django.urls import path
from . import views
urlpatterns = [
    path('', views.hoome, name='home'),
    path('students/<int:id>/', views.detail, name='student-detail'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('students/', views.student_list, name='student-list'),
]

