from django.urls import path
from .views import PostListView, PostDetailView, PostCreateview, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path("", PostListView.as_view(), name="blog-home"),
    path("about/", views.about, name="blog-about"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateview.as_view(), name="post-create"),
    path("post/<int:pk>/update", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="post-delete"),

]