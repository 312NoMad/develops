from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UpvoteView, PostViewSet, CommentViewSet

router = DefaultRouter()
router.register('', PostViewSet)
router.register('comment', CommentViewSet)
urlpatterns = [
    path('upvote/<int:pk>', UpvoteView.as_view()),
    path('', include(router.urls))
]
