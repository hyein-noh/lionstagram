from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('publish')
    content = models. TextField()

    def __str__(self):
        return self. title
      