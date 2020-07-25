from django.db import models
from django.utils import timezone


class OGInterface(models.Model):
    """
    Open Graph library for the parsing Open Graph markup
    """
    name = models.CharField(max_length=50, verbose_name='Name of the interface')
    description = models.CharField(max_length=200, verbose_name='Description of the interface',
                                   blank=True)
    github_link = models.URLField(verbose_name='Link to GitHub repository of the interface')
    module_name = models.CharField(max_length=50,
                                   verbose_name='Name of the python module '
                                                'where a parser class should be stored')
    class_name = models.CharField(max_length=50, verbose_name='Name of a class name for a parser')


class UrlHistory(models.Model):
    """
    Stores the last N parsed urls.
    Amount of N could be specified in the settings.
    """
    url = models.URLField(verbose_name='Url link for parsing', unique=True)
    created_at = models.DateTimeField(verbose_name='Date and Time when url was created',
                                      auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Date and Time when url was created',
                                      auto_now=True)
