from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    picture = models.ImageField(blank=True)
    content = models.TextField(blank=True)
    site_url = models.URLField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title

class Comment(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments_post')

    def __str__(self):
        return self.content

