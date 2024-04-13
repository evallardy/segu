from django.urls import path
from .views import ClienteListView, ClienteDetailView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView, Domicilio_cliente

urlpatterns = [
    path('', ClienteListView.as_view(), name='cliente_list'),
    path('<int:pk>/', ClienteDetailView.as_view(), name='cliente_detail'),
    path('nuevo/', ClienteCreateView.as_view(), name='cliente_create'),
    path('<int:pk>/editar/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('<int:pk>/eliminar/', ClienteDeleteView.as_view(), name='cliente_delete'),
    path('domicilio_cliente/<int:pk>/', Domicilio_cliente.as_view(), name='domicilio_cliente'),
]