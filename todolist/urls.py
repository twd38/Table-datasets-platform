"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from todo.views import register, addPost, createPost, deletePost, searchResults, updateSettings
# from todo.views import addTodo, deleteTodo, subItemView, addSubItem,
#  deleteSubItem, register, addPost, createPost, deletePost

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('todo/', todoView),
    # path('addTodo/', addTodo),
    # path('deleteTodo/<int:todo_id>/', deleteTodo),
    # path('subItemView/', subItemView),
    # path('addSubItem/', addSubItem),
    # path('deleteSubItem/<int:subItem_id>/', deleteSubItem),
    #new stuff
    path('accounts/', include('django.contrib.auth.urls')),
    path('updateSettings/', updateSettings),
    path('', include('todo.urls')),
    path('register/', register),
    #new stuff two
    path('addPost/', addPost),
    path('createPost/', createPost),
    path('deletePost/<int:post_id>/', deletePost),
    path('searchResults/', searchResults)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)