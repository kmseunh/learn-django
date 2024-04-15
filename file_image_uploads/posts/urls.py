from django.urls import path

from .views import CreatePostView, HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("post/", CreatePostView.as_view(), name="add_post"),
]
