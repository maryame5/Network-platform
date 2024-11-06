from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

   

class Post(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="emails")
    content = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)
    followers = models.ManyToManyField(User, through='follow' , through_fields=('post_fo', 'follower'),related_name='followed_post')
    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "like": self.like,
          
        }
    
class follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE,related_name="following")
    following = models.ForeignKey(User, on_delete=models.CASCADE,related_name="followers")
    post_fo = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post_following', null=True, blank=True)
    def __str__(self):
        return f"{self.follower.username} is following {self.following.username}"
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post',)
