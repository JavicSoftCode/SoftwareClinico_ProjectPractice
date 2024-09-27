from django.shortcuts import render
from django.views import View


class HomeView(View):
  template_name = 'core/home.html'  # Plantilla que se va a renderizar

  # Método GET para manejar solicitudes de tipo GET
  def get(self, request, *args, **kwargs):
    # Aquí puedes definir todo el contexto necesario para la plantilla
    context = {
      'title': 'Software Clinico',
      'title_h1': 'SoftClinico - Sistema Médico',
      'descriptions_p': 'Soluciones tecnológicas avanzadas para la gestión clínica',
      'title_h2': 'Nuestros Servicios',

    }
    # Renderiza la plantilla con el contexto
    return render(request, self.template_name, context)
