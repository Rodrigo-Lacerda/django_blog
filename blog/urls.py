from django.urls import path

from .views import Post, PostList

urlpatterns = [
        path('<slug:slug>/', Post.as_view(), name='post_detail'),
        path('', PostList.as_view(), name='post_list'),
        ]

