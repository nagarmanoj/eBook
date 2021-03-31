from django.db import models

# Create your models here.
#Django Blog App Database
# 1 post
# 2 Category
# 3 Comment

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
    image = models.FilePathField(path="/images")
    categories = models.ManyToManyField('Category',related_name="posts")

class Category(models.Model):
    name = models.CharField(max_length=20)

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post',on_delete = models.CASCADE)
