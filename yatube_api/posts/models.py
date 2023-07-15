from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
MAX_LENGTH = 15


class Group(models.Model):
    title = models.CharField('Название сообщества', max_length=200)
    slug = models.SlugField('Идентификатор', unique=True)
    description = models.TextField('Описание сообщества',)

    class Meta:
        verbose_name = 'сообщество'
        verbose_name_plural = 'Сообщества'

    def __str__(self):
        return self.title[:MAX_LENGTH]


class Post(models.Model):
    text = models.TextField("Текст поста")
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts',
        verbose_name='Автор поста'
    )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True,
        verbose_name='Картинка'
    )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name='posts', blank=True, null=True,
        verbose_name='Группа'
    )

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.text[:MAX_LENGTH]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments',
        verbose_name='Автор комментария',
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments',
        verbose_name='Пост'
    )
    text = models.TextField('Текст комментария',)
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:MAX_LENGTH]


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower'
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following'
    )

    class Meta:
        unique_together = ('user', 'following')
        verbose_name = 'подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_user_following'
            )
        ]

    def __str__(self):
        return self.user[:MAX_LENGTH]
