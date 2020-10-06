from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse
import os

class Post(models.Model):
    title=models.CharField(max_length=100)
    file=models.FileField(null=True,blank=True,upload_to='Files')
    content=models.TextField()
    data_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def extension(self):
        name,extension=os.path.splitext(self.file.name)
        return extension

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})


