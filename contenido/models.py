from django.db import models


class materia(models.Model):
  topico = models.CharField(blank=False, null=False, max_length=255)
  subtopico = models.CharField(blank=False, null=False, max_length=255)
  def __str__(self):
    return u'%s' % (self.topico+" -> "+self.subtopico)
