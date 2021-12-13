from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=70)
    slug=models.SlugField(max_length=70,unique=True)
    img=models.ImageField(upload_to='productcategory')

    def __str__(self):
        return self.name

class Product(models.Model):
    product_id=models.AutoField
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=50)
    slug=models.SlugField(unique=True)
    desc=models.TextField(max_length=300)
    img=models.ImageField(upload_to='productimages')
    url=models.URLField()
    price=models.IntegerField()
    pub_date=models.DateField()

    def __str__(self):
        return self.product_name[:15]

