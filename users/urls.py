from django.urls import path

from . import views
from .views import (
    login_view,
    send_friend_request,
    accept_friend_request,
    friend_list,
    signup_view,
    home_view
)

urlpatterns = [
    path('send-friend-request/<int:user_id>/', send_friend_request, name='send-friend-request'),
    path('accept-friend-request/<int:friendship_id>/', accept_friend_request, name='accept-friend-request'),
    path('friends/<int:user_id>/', friend_list, name='friend-list'),
    path('signup/', signup_view, name='signup'),
    path('home/', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('users/', views.user_list_view, name='list_friends'),
    # ... otras URLs de la aplicación 'users' si las hay ...
]
