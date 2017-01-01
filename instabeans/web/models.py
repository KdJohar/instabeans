from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Seo(models.Model):
    PAGES = (
        ('home','home'),
        ('work','work'),
        ('contact','contact')
    )
    page = models.CharField(max_length=100, choices=PAGES, unique=True)
    title = models.CharField(max_length=500)
    keywords = models.TextField()
    description = models.TextField()

    def __unicode__(self):
        return self.page


class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    contact_no = models.CharField(max_length=500, blank=None, null=True)
    skype_id = models.CharField(max_length=500, blank=None, null=True)
    profile_url = models.URLField(blank=None, null=True)
    image = models.ImageField(upload_to='client/')
    profile = models.CharField(max_length=500, blank=None, null=True)
    company = models.CharField(max_length=500, blank=None, null=True)

    class Meta:
        unique_together = ("name", "email")

    def __unicode__(self):
        return self.name

class Testimonial(models.Model):
    client = models.OneToOneField(Client)
    testimonial = models.TextField()

    def __unicode__(self):
        return self.client.name

class ProjectCategory(models.Model):
    name = models.CharField(unique=True, max_length=255)

    def __unicode__(self):
        return self.name


class Project(models.Model):
    client = models.ForeignKey(Client)
    name = models.CharField(max_length=255, unique=True)
    category = models.ManyToManyField(ProjectCategory)
    image = models.ImageField(upload_to='projects/')
    description = models.TextField()
    url = models.URLField(unique=True)


    def __unicode__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.name