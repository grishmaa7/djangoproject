from django.urls import path
from teachers import views

urlpatterns = [
    path('name/', views.home, name='home'),
    path('aboutus/', views.About_Us, name='about_us'),
    path('contact/', views.Contact, name='contact'),
]