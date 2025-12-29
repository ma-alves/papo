from django.urls import path

from . import views

# urls sem parâmetros vão primeiro!
urlpatterns = [
	path('', views.home, name='home'),
	path('search/', views.search_users, name='search'),
	path('profile/<str:username>/', views.UserDetailView.as_view(), name='profile'),
	path('start-chat/<str:username>/', views.get_or_create_chat, name='start-chat'),
    path('delete-chat/<uuid:chat_uuid>/', views.delete_chat, name='delete-chat'),
	path('<uuid:chat_uuid>/', views.chat_view, name='chat'),
]
