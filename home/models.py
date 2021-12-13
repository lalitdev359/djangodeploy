from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=50)
    contactno=models.IntegerField()
    email=models.EmailField(max_length=100)
    msg=models.CharField(max_length=1000)

    def __str__(self):
        return self.username + " " + self.msg[:10]
