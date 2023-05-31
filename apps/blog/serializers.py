from rest_framework import serializers

from apps.accounts.serializers import UserListSerializer
from apps.blog.models import Comment, Like, Post, Tag


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class TagCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("name",)


class LikeListSerializer(serializers.ModelSerializer):
    user = UserListSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ("id", "user", "post", "comment")


class LikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ("user", "post", "comment")


class CommentListSerializer(serializers.ModelSerializer):
    user = UserListSerializer(read_only=True)
    likes = LikeListSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "user", "post", "text", "likes")


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "user", "post", "text")


class PostListSerializer(serializers.ModelSerializer):
    author = UserListSerializer(read_only=True)
    tags = TagListSerializer(many=True, read_only=True)
    last_comments = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    total_comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "id",
            "author",
            "title",
            "content",
            "publication_date",
            "category",
            "tags",
            "last_comments",
            "likes",
            "total_comments",
        )

    def get_likes(self, obj):
        return obj.like_set.count()

    def get_last_comments(self, obj):
        comments = Comment.objects.filter(post=obj).order_by("-id")[:3]
        return CommentListSerializer(comments, many=True).data

    def get_total_comments(self, obj):
        return obj.comment_set.count()


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "author",
            "title",
            "content",
            "publication_date",
            "category",
            "tags",
        )
