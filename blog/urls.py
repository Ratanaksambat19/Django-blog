from django.urls import path
from . import views
from user import views as user_view
from .views import (PostDetailView, 
                    PostListView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView)

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name = 'home'),
    path('user/<str:username>', UserPostListView.as_view(), name = 'user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),
    path('movie/', views.movie, name = 'movie'),
    path('sport/', views.sport, name = 'sport'),
    path('travel/', views.travel, name = 'travel'),
]