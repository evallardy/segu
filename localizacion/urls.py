from django.urls import path

from .views import LocalizacionLugar

urlpatterns = [
    path('localizacion/', LocalizacionLugar.as_view(), name='localizacion_lugar'),
]
