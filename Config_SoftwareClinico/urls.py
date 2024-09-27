from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                path('admin/', admin.site.urls),
                path('', include('BackEnd.Apps.core.urls', namespace='core')),  # Incluir las URLs de core en la raíz
                path('doctor/', include('BackEnd.Apps.Crud_Doctor.urls', namespace='doctor')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
