from django.urls import path

from .views import Post, PostList, PostUpdate

urlpatterns = [
        path('<slug:slug>/', Post.as_view(), name='post_detail'),
        path('', PostList.as_view(), name='post_list'),
        path('update/', PostUpdate.as_view(), name='post_update'),
        ]

