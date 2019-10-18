from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Article(models.Model):
    title=models.CharField(max_length=98,)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateField(auto_now_add=True)
    # add in thumbnail later
    thumb=models.ImageField(default='default.png',blank=True)
    # add in author later
    author=models.ForeignKey(User,default=None,on_delete='CASCAD')

    def __str__(self):
        return self.title
    
    def snippet(self):
        if self.body != '':
            return self.body[:50]+'....'
        else:
            return self.body