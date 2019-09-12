from django.db import models


class Archivo(models.Model):
  ruta = models.CharField(blank=False, null=False, max_length=255)
  dificultad = models.IntegerField(blank=False, null=False)
  materia = models.ForeignKey('contenido.Materia',on_delete=models.CASCADE)
  semestre = models.IntegerField(blank=True, null=False)
  anio = models.IntegerField(blank=True, null=False)
