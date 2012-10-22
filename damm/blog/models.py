
from django.db import models


class BlogPost(models.Model):

    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    published = models.BooleanField()
    publish_date = models.DateTimeField()
    content = models.TextField()

    def __unicode__(self):
        return self.title

    def admin_link(self):
        return "<a href='#'>View on site</a>"
    admin_link.allow_tags = True
    admin_link.short_description = ""


class Homepage(models.Model):

    content = models.TextField()

    class Meta:
        verbose_name_plural = "Homepage"

    def __unicode__(self):
        return ""
