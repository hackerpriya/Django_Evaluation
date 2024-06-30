from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.list_users, name='list_users'),
    path('users/<int:user_id>/', views.user_details, name='user_details'),
    path('services/', views.list_services, name='list_services'),
    path('services/<str:type>/', views.service_details, name='service_details'),
    path('subscription/', views.create_subscription_view, name='create_subscription'),
]
