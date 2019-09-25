from django.db import models

class Usuario(models.Model):
  email = models.CharField(primary_key=True, blank=False, null=False, max_length=255)
  nombre = models.CharField(blank=False, null=False, max_length=255)
  def __str__(self):
    return u'%s' % self.email



