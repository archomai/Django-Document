import datetime

from django.db import models
from django.utils import timezone

__all__ = (
    'Post',
    'User',
    'PostLike',
)


class Post(models.Model):
    title = models.CharField(max_length=50)
    like_users = models.ManyToManyField(
        'User',
        through='PostLike',
        related_name='like_posts',
    )

    class Meta:
        verbose_name_plural = 'Intermidiate - Post'

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Intermidiate - User'

    def __str__(self):
        return self.name


class PostLike(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name_plural = 'Intermidiate - PostLike'

    def __str__(self):
        # 글 title이 "공지사항"이며
        # 유저 name이 "이한영"이고,
        # 좋아요 누른 시점이 2018.01.31일때
        # "공지사항"글의 좋아요(이한영, 2018.01.31)으로 출력
        return '"{title}"글의 좋아요({name}, {date})'.format(
            title=self.post.title,
            name=self.user.name,
            date=datetime.strftime(
                # timezone.make_naive(self.created_date),
                timezone.localtime(self.created_date),
                '%Y.%m.%d'),
        )
