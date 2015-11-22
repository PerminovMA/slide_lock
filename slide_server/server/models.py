from django.db import models
from django.contrib.auth.models import AbstractUser


class Token(models.Model):
    token = models.CharField(max_length=50)
    produce = models.DateTimeField()

    def __unicode__(self):
        return self.token


class Country(models.Model):
    country_name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.country_name


class City(models.Model):
    city_name = models.CharField(max_length=50)
    location = models.ForeignKey(Country)

    def __unicode__(self):
        return self.city_name


class UserProfile(AbstractUser):
    device_id = models.CharField(max_length=50)
    reg_date = models.DateField(auto_now_add=True)
    last_change = models.DateField(auto_now=True)
    city = models.ForeignKey(City, null=True, blank=True)
    token = models.ForeignKey(Token, null=True)

    AbstractUser._meta.get_field('email')._unique = True  # Make email field unique
    AbstractUser._meta.get_field('username')._unique = False  # Make username field not unique

    def __unicode__(self):
        return str(self.email)


class Error(models.Model):
    explanation = models.CharField(max_length=100, null=True, blank=True)
    error_id = models.CharField(max_length=10, null=True, blank=True)
    user = models.ForeignKey(UserProfile, null=True, blank=True)
    function_name = models.CharField(max_length=100, null=True, blank=True)
    error_date_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.explanation)


class VKImageCategory(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    previewImgURL = models.CharField(max_length=150, null=False, blank=False)  # preview image URL location
    count_views = models.PositiveIntegerField(null=False, blank=False, default=0)

    def __unicode__(self):
        return str(self.name)


class VKAlbum(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    category = models.ForeignKey(VKImageCategory)
    vk_group_id = models.CharField(max_length=20, null=False, blank=False)
    vk_album_id = models.CharField(max_length=20, null=False, blank=False)
    preview_img_URL = models.CharField(max_length=150, null=False, blank=False)  # preview image URL location

    def __unicode__(self):
        return str(self.name)
