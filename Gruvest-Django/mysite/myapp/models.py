from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class PostModel(models.Model):
    header = models.CharField(max_length=100)
    post = models.CharField(max_length=240)
    upVotes = models.IntegerField(default=0)
    downVotes = models.IntegerField(default=0)

    def __str__(self):
        return self.post
    
    def getUpVotes(self):
        return self.upVotes
    
    def getDownVotes(self):
        return self.downVotes

    def getTotalVotes(self):
        return self.upVotes - self.downVotes

class CommentModel(models.Model):
    comment = models.CharField(max_length=240)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self):
        return self.comment

class UpvoteModel(models.Model):
    upvoter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='upvote_user')
    upvotedPost = models.ForeignKey('PostModel', on_delete=models.CASCADE, related_name='upvoted_post')

class DownvoteModel(models.Model):
    downvoter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='downvote_user')
    downvotedPost = models.ForeignKey('PostModel', on_delete=models.CASCADE, related_name='downvoted_post')

    