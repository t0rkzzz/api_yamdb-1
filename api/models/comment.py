from django.db import models

from .review import Review
from .user import User


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="id публикации",
    )
    text = models.TextField(
        verbose_name="Текст комментария",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="username автора комментария"
    )
    pub_date = models.DateTimeField(
        "Дата публикации комментария",
        auto_now_add=True
    )

    class Meta:
        ordering = ["-pub_date"]

    def __str__(self):
        return self.text
