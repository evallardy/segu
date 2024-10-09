from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.urls.conf import include

from core.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('arma/', include('armamento.urls')),
    path('cliente/', include('cliente.urls')),
    path('rh/', include('rh.urls')),
    path('vehiculo/', include('vehiculo.urls')),
    path('asignacion/', include('asignacion.urls')),
    path('localizacion/', include('localizacion.urls')),
    path('seguimiento/', include('seguimiento.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    re_path(r'^static/(?P<path>.*)$', serve, {
        'document_root': settings.STATIC_ROOT
    }),
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT
    }), 
]