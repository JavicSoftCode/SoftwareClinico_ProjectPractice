from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import DoctorForm
from .models import Doctor


class DoctorListView(ListView):
  model = Doctor
  template_name = 'app_crud_doctor/DoctorList.html'  # Ruta del template para listar doctores
  context_object_name = 'doctores'  # Nombre con el que accedemos a la lista de doctores en el template
  paginate_by = 10  # Paginar si hay más de 10 doctores (opcional)


class DoctorCreateView(CreateView):
  model = Doctor
  form_class = DoctorForm  # Campos que se mostrarán en el formulario
  template_name = 'app_crud_doctor/DoctorForm.html'  # Ruta del template para el formulario
  success_url = reverse_lazy('Crud_Doctor:doctor_list')  # Redireccionar después de crear


class DoctorUpdateView(UpdateView):
  model = Doctor
  form_class = DoctorForm  # Campos que se mostrarán en el formulario
  template_name = 'app_crud_doctor/DoctorForm.html'  # Se puede reutilizar el mismo template que `CreateView`
  success_url = reverse_lazy('Crud_Doctor:doctor_list')  # Redireccionar después de actualizar


class DoctorDeleteView(DeleteView):
  model = Doctor
  template_name = 'app_crud_doctor/DoctorDelete.html'  # Template de confirmación
  success_url = reverse_lazy('Crud_Doctor:doctor_list')  # Redireccionar después de eliminar
