from django.db import models

# Create your models here.


class Tweet(models.Model):
    body = models.CharField(max_length=255)
    is_retweet = models.BooleanField(default=False)
    author = models.ForeignKey('auth.User', related_name='tweets', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body
    class Meta:
        ordering = ['created_at']

