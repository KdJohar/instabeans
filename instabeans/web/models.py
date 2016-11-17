from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Seo(models.Model):
    title = models.CharField(max_length=500)
    keywords = models.TextField()
    description = models.TextField()

    def __unicode__(self):
        return 'SEO'
