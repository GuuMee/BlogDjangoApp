from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #arguments can be: (auto_now = True)- it will automatically update to the current date with updating post or (auto_now_add = True) - it will not change even not edit the date after creating the post
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
