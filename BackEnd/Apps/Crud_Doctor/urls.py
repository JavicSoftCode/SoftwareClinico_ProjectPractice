from django.urls import path
from .views import DoctorListView, DoctorCreateView, DoctorUpdateView, DoctorDeleteView

app_name = 'Crud_Doctor'

urlpatterns = [
    path('doctores/', DoctorListView.as_view(), name='doctor_list'),
    path('doctores/nuevo/', DoctorCreateView.as_view(), name='doctor_create'),
    path('doctores/editar/<int:pk>/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctores/eliminar/<int:pk>/', DoctorDeleteView.as_view(), name='doctor_delete'),
]
