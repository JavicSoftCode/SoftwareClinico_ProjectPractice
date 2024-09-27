from django import forms

from .models import Doctor


class DoctorForm(forms.ModelForm):
  class Meta:
    model = Doctor
    fields = ['cedula', 'nombre', 'estado', 'image']  # Cambia 'imagen' a 'image' para que coincida con el modelo

  def clean_image(self):  # Cambia 'imagen' a 'image'
    image = self.cleaned_data.get('image')  # Cambia 'imagen' a 'image'
    if image:
      # Ya no es necesario validar aquí ya que estamos usando FileExtensionValidator en el modelo
      return image
    return image  # Devuelve la imagen si es válida
