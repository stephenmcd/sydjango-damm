
from django.db import models


class BlogPost(models.Model):

    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    published = models.BooleanField()
    publish_date = models.DateTimeField()
    content = models.TextField()

    def __unicode__(self):
        return self.title
