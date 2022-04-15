from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from .models import Post, Upvote, Comment
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UpvoteView(APIView):
    def post(self, request, pk):
        user = request.user
        post = Post.objects.get(id=pk)
        queryset = Upvote.objects.create(author=user,
                                         post=post,
                                         value=True)
