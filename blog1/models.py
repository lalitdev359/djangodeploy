from django.db import models


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=70)
    slug=models.SlugField(max_length=70,unique=True)
    img=models.ImageField(upload_to='categorypics')

    def __str__(self):
        return self.name

    # @property
    # def image_url(self):
    #     if self.img and hasattr(self.img,'url'):
    #         return self.img.url

class Post(models.Model):
    title=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    desc=models.TextField()
    img=models.ImageField(upload_to='postimages')
    slug=models.CharField(max_length=100,unique=True)
    author=models.CharField(max_length=40)
    timestamp=models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + "by" + self.author

    # @property
    # def image_url(self):
    #     if self.img and hasattr(self.img,'url'):
    #         return self.img.url
    

   

