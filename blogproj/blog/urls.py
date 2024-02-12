from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    # existing patterns
    path('about/', views.about, name="blog-about"),

    path('', PostListView.as_view(), name="blog-home"),
    path('post-new/', PostCreateView.as_view(), name="blog-new"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="blog-detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="blog-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="blog-delete"),

    # Logout view
    path('logout/', LogoutView.as_view(), name='logout'),
]
