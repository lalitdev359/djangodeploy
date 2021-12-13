from django.db import models
from django.db.models.deletion import CASCADE
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=30)
    img=models.ImageField(upload_to='videocatpics', blank=True)
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.name
        

class Item(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)
    img=models.ImageField(upload_to='videothumbnail')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    video=EmbedVideoField()
    desc=models.TextField()
    publish=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class VideoComment(models.Model):
    srno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    video=models.ForeignKey(Item,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[:15] + "by" + self.user.username

