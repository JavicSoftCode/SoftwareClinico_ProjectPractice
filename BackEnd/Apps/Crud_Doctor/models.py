from django.core.validators import FileExtensionValidator

from django.db import models


class Doctor(models.Model):
  STATUS_CHOICES = [
    ('active', 'Activo'),
    ('inactive', 'Inactivo'),
  ]

  # Para trabajar unicamente con archivos de imagenes  pip install Pillow
  image = models.ImageField(
    upload_to='app_crud_doctor/images',
    validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'svg', 'webp'])],
    verbose_name="Foto Del Doctor"
  )
  cedula = models.CharField(max_length=10, unique=True, verbose_name="Cédula")
  nombre = models.CharField(max_length=100, verbose_name="Nombre Completo")
  estado = models.CharField(
    max_length=8,
    choices=STATUS_CHOICES,
    default='active',
    verbose_name="Estado"
  )

  def __str__(self):
    return f"{self.nombre} - {self.cedula}"

  class Meta:
    verbose_name = "Doctor"
    verbose_name_plural = "Doctores"
    ordering = ['nombre']
