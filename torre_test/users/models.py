from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(verbose_name=_("Name of User"), blank=True, max_length=120)
    headline = models.CharField(verbose_name=_('Headline'), max_length=160, default='')
    location = models.CharField(verbose_name=_('Location'), max_length=120, default='')
    summary = models.TextField(verbose_name=_('Summary of your bio (optional)'), blank=True, default='')
    extra_data = JSONField(verbose_name=_('Extra Data'), default=dict)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class UserJob(models.Model):
    role = models.CharField(verbose_name=_('Role'), max_length=255)
    company_name = models.CharField(verbose_name=_('Company Name'), max_length=255)
    from_month = models.CharField(verbose_name=_('From Month'), max_length=255)
    from_year = models.CharField(verbose_name=_('From Year'), max_length=255)
    to_month = models.CharField(verbose_name=_('To Month'), max_length=255, blank=True)
    to_year = models.CharField(verbose_name=_('To Year'), max_length=255, blank=True)
    is_current = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name='jobs', verbose_name=_('User'), on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-from_year', '-from_month']
    
    def __str__(self):
        return self.role


class UserSocialLink(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    url = models.CharField(verbose_name=_('Url'), max_length=255)
    user = models.ForeignKey(User, related_name='links', verbose_name=_('User'), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
