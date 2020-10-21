from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class article(models.Model):
    title = models.CharField( max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} article"

class article_image(models.Model):
    article = models.OneToOneField(article, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="article_pics")

    def __str__(self):
        return f"{self.article.title}"