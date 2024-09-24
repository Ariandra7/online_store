from django.db import models

# Create your models here.
class Person(models.Model):
      name = models.CharField(max_length=100)
      age = models.IntegerField()

class Post(models.Model):
    title = models.CharField(max_length=200) # заголовок поста
    content = models.TextField()  # содержание поста
    created_at = models.DateTimeField(auto_now_add=True) # созданный пост
    def __str__(self):
        return self.title

     
