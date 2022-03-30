from django.urls import path
from .views import News, Search, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView, UserUpdateView

urlpatterns = [
    path('', News.as_view()),
    # path('<int:pk>', News.as_view()),
    path('search/', Search.as_view()),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('user_update/<int:pk>', UserUpdateView.as_view(), name='user_update'),
]