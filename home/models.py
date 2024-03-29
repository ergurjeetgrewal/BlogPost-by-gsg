from django.db import models

# Create your models here.


class Contact(models.Model):
    s_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    desc = models.TextField(default="")
    res_time=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.name
