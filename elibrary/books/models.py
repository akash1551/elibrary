from django.db import models
from time import time

def get_upload_file_name(instance, filename):
    return "images/%s_%s" %(str(time()).replace('.','_'),filename.replace(' ', '_'))


class Books(models.Model):
    book_name=models.CharField(max_length=100)
    author_name=models.CharField(max_length=100)
    description=models.CharField(max_length=5000)
    thumbnail=models.FileField(upload_to=get_upload_file_name)
    tag = models.TextField()
    category = models.TextField()



# Create your models here.
