from .views import user_login, register, user_logout
from django.urls import path

urlpatterns = [
    path('login/', user_login, name='user_login'),   
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),   


]