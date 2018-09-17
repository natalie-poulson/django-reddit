from django.urls import path
from . import views 

urlpatterns= [
    path('', views.post_list, name='post_list'),
    path('posts/<int:pk>', views.post_detail, name='post_detail'),
    path('posts/new', views.post_create, name='post_create'),


    path('register', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
    path('logout', views.user_logout, name='logout'),
    path('special', views.special, name='special'),

    path('comment/new', views.comment_create, name='comment_create')
]