from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    author = models.ForeignKey('Author',on_delete=models.CASCADE)
    image = models.ImageField()
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Author(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.EmailField()
    cellphone_num = models.IntegerField()

    def __str__(self):
        return self.user.username

