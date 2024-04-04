from django.urls import path
from .views import *

urlpatterns = [
    path('armas/', ArmaListView.as_view(), name='arma_list'),
    path('armas/crear/', ArmaCreateView.as_view(), name='arma_create'),
    path('armas/<int:pk>/', ArmaDetailView.as_view(), name='arma_detail'),
    path('armas/<int:pk>/actualizar/', ArmaUpdateView.as_view(), name='arma_update'),
    path('armas/<int:pk>/eliminar/', ArmaDeleteView.as_view(), name='arma_delete'),
]
