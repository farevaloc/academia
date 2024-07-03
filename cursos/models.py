from django.db import models

from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    ROLES = (
        ('admin', 'Administrador'),
        ('normal', 'Usuario Normal'),
    )

    rol = models.CharField(max_length=7, choices=ROLES, default='normal')


class Curso(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cupos = models.PositiveIntegerField()
    estado = models.BooleanField(default=True)
    inscritos = models.ManyToManyField(Usuario, related_name='cursos_inscritos', blank=True)

    def __str__(self):
        return self.nombre 

