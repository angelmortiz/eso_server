import debug_toolbar
from django.contrib import admin
from django.urls import path, include

# Customizing admin panel header
admin.site.site_header = 'En Salud Optima Admin'

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'auth/', include('djoser.urls')),
    path(r'auth/', include('djoser.urls.jwt')),
    path(r'v1/', include('core.urls')),
    path(r'v1/fitness/', include('fitness.urls')),
    path(r'__debug__/', include(debug_toolbar.urls))
]
