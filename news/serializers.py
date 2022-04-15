from rest_framework.serializers import ModelSerializer

from .models import Post, Upvote, Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('author', 'post', 'creation_date')


class PostSerializer(ModelSerializer):
    comments = CommentSerializer()

    class Meta:
        model = Post
        fields = ('title', 'link', 'creation_date', 'content', 'author', 'comments', 'upvote')
