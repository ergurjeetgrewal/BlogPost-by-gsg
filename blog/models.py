from django.db import models

# Create your models here.


class Post(models.Model):
    s_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=220)
    content=models.TextField()
    author = models.CharField(max_length=13)
    timestamp = models.DateTimeField(blank=True)
    slug = models.CharField(max_length=130,default='')
    def __str__(self):
        return self.title +' '+ self.author

