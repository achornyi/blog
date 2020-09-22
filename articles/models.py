from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    tags = ArrayField(models.CharField(max_length=50, blank=True, unique=True))
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    @property
    def last_update(self):
        return self.updated_on or self.created_on
