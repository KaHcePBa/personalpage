from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy

User = get_user_model()  # лучше всего использовать такой способ модели юзера


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                               blank=True)  # CASCADE - при удалении пользователя удаляются и его посты
    # SET_NULL - обнуляет ключевые поля при удалении юзера
    title = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy("blog:post", kwargs={"pk": str(self.pk)})
