from rest_framework import serializers

from posts.models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    likes_number = serializers.SerializerMethodField()
    author_username = serializers.SerializerMethodField()
    time_created = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "pk",
            "content",
            "time_created",
            "author",
            "likes_number",
            "author_username",
        ]

    def get_likes_number(self, obj):
        if isinstance(obj, dict):
            post_id = obj["pk"]
        elif isinstance(obj, Post):
            post_id = getattr(obj, "pk")

        return Like.objects.filter().count()

    def get_author_username(self, obj):
        if isinstance(obj, dict):
            return obj["author__username"]
        elif isinstance(obj, Post):
            return getattr(getattr(obj, "author"), "username")

    def get_time_created(self, obj):
        if isinstance(obj, Post):
            return getattr(obj, "time_created").strftime("%H:%M %B %d, %Y")

        return obj["time_created"].strftime("%H:%M %B %d, %Y")


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = [
            "post_id",
        ]
