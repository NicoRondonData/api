from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, LikeViewSet, PostViewSet, TagViewSet

router = DefaultRouter()
router.register(r"tags", TagViewSet, basename="tags")
router.register(r"posts", PostViewSet, basename="posts")
router.register(r"comments", CommentViewSet, basename="comments")
router.register(r"likes", LikeViewSet, basename="likes")
urlpatterns = [
    path("blog/", include(router.urls)),
]
