from django.db import models
from django.contrib.auth.models import User


class materia(models.Model):
  topico = models.CharField(blank=False, null=False, max_length=255)
  subtopico = models.CharField(blank=False, null=False, max_length=255)
  def __str__(self):
    return u'%s' % (self.topico+" -> "+self.subtopico)


class estudio(models.Model):
  ruta = models.CharField(blank=False, null=False, max_length=255)
  materia = models.ForeignKey('contenido.materia', on_delete=models.CASCADE)
  nombre = models.CharField(blank=False, null=False, max_length=100)
  def __str__(self):
    return u'%s' % self.nombre


class estudio_usuario(models.Model):
  estudio = models.ForeignKey('contenido.estudio', on_delete=models.CASCADE)
  usuario = models.ForeignKey(User, on_delete=models.CASCADE)
  fecha = models.DateField(auto_now_add=True, null=True)

  class Meta:
    unique_together = (("estudio", "usuario"),)

  def __str__(self):
    return u'%s' % self.estudio.nombre
