from django.urls import path, include
from . import views

urlpatterns = [
    path('', include(views.router.urls)),
    path('user-data', views.get_current_user),
    path('get-message', views.get_messages),
    path('get-chats', views.get_chats),
    path('search-users', views.search_user),
]