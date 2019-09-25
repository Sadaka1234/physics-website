from django.db import models


class Ejercicio(models.Model):
  ruta = models.CharField(blank=False, null=False, max_length=255)
  dificultad = models.IntegerField(blank=False, null=False)
  materia = models.ForeignKey('contenido.Materia', on_delete=models.CASCADE)
  semestre = models.IntegerField(blank=True, null=False)
  anio = models.IntegerField(blank=True, null=False)

  def __str__(self):
    return u'%s' % self.ruta


class ejercicio_usuario(models.Model):
  ejercicio = models.ForeignKey('preguntas.Ejercicio', on_delete=models.CASCADE)
  usuario = models.ForeignKey('home.Usuario', on_delete=models.CASCADE)
  resuelto = models.BooleanField(null=False)

  class Meta:
    unique_together = (("ejercicio", "usuario"),)

  def __str__(self):
    if self.resuelto == True:
      return u'%s' % self.usuario + " -> " + self.ejercicio.ruta + " RESUELTO"
    else:
      return u'%s' % self.usuario + " -> " + self.ejercicio.ruta + " NO-RESUELTO"
