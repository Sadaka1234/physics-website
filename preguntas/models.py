from django.db import models
from django.contrib.auth.models import User
from django import forms

class ejercicio(models.Model):
  ruta = models.CharField(blank=False, null=False, max_length=255)
  dificultad = models.IntegerField(blank=False, null=False)
  materia = models.ForeignKey('contenido.materia', on_delete=models.CASCADE)
  semestre = models.IntegerField(blank=True, null=False)
  anio = models.IntegerField(blank=True, null=False)
  nombre = models.CharField(blank=False, null=False, max_length=255)

  def __str__(self):
    return u'%s' % self.ruta


class ejercicio_usuario(models.Model):
  ejercicio = models.ForeignKey('preguntas.ejercicio', on_delete=models.CASCADE)
  usuario = models.ForeignKey(User, on_delete=models.CASCADE)
  resuelto = models.BooleanField(null=False)

  class Meta:
    unique_together = (("ejercicio", "usuario"),)

  def __str__(self):
      return u'%s' % self.ejercicio.ruta

class certamen(models.Model):
  nombre = models.CharField(blank=False, null=False, max_length=255, default="certamen")
  fecha = models.DateField(blank=False, null=False)
  usuario = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return u'%s' % self.nombre

class certamen_pregunta(models.Model):
  certamen = models.ForeignKey('preguntas.certamen', on_delete=models.CASCADE)
  pregunta = models.ForeignKey('preguntas.ejercicio', on_delete=models.CASCADE)
