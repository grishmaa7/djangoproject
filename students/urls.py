from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.home, name='home'),
    path('students/<int:id>/', views.detail, name='student-detail'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('list/', views.student_list, name='student-list'),
]