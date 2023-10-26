import debug_toolbar
from django.contrib import admin
from django.urls import path, include

# Customizing admin panel header
admin.site.site_header = 'En Salud Optima Admin'

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('v1/fitness/', include('fitness.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]
