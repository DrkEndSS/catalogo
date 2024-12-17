from django.contrib import admin
from django.urls import path, include  # Agrega 'include' para incluir las URLs de productos

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el panel de administración
    path('', include('productos.urls')),  # Incluye las URLs de la aplicación productos
]
