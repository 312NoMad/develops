from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=100)
    link = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='posts')

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comments')
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} commented {self.post}'


class Upvote(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='upvote')
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='upvote')
    value = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.author} >>> {self.post}'
