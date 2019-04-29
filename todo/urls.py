from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/register/', views.register, name='register'),
    path('userPosts/<int:user_id>', views.userPosts, name='userPosts'),
    path('singleTable/<int:post_id>', views.singleTable, name='singleTable')
]
