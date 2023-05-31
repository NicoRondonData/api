from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import decorators, filters, response, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.accounts.permissions import IsOwnerOrAdminOrReadOnly
from apps.blog.models import Comment, Like, Post, Tag
from apps.blog.serializers import (
    CommentCreateSerializer,
    CommentListSerializer,
    LikeCreateSerializer,
    LikeListSerializer,
    PostCreateSerializer,
    PostListSerializer,
    TagCreateSerializer,
    TagListSerializer,
)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return TagListSerializer
        return TagCreateSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [IsOwnerOrAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["title", "author__username", "category", "tags__name"]
    search_fields = ["title", "author__username", "category", "tags__name"]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return PostListSerializer
        return PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @decorators.action(detail=True, methods=["get"])
    def likes(self, request, pk=None):
        post = self.get_object()
        likes = Like.objects.filter(post=post)
        serializer = LikeListSerializer(likes, many=True)
        return response.Response(serializer.data)

    @decorators.action(detail=True, methods=["get"])
    def comments(self, request, pk=None):
        post = self.get_object()
        comments = Comment.objects.filter(post=post)
        serializer = CommentListSerializer(comments, many=True)
        return response.Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [IsOwnerOrAdminOrReadOnly]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return CommentListSerializer
        return CommentCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @decorators.action(detail=True, methods=["get"])
    def likes(self, request, pk=None):
        comment = self.get_object()
        likes = Like.objects.filter(comment=comment)
        serializer = LikeListSerializer(likes, many=True)
        return response.Response(serializer.data)


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    permission_classes = [IsOwnerOrAdminOrReadOnly]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return LikeListSerializer
        return LikeCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
