from django.urls import path
from .views import AsigancionListView, AsignacionCreateView, AsignacionUpdateView, AsignacionDeleteView, asignar_empleado

urlpatterns = [
    path('asignaciones/', AsigancionListView.as_view(), name='asigancion_list'),
    path('crear/', AsignacionCreateView.as_view(), name='asignacion_create'),
    path('<int:pk>/editar/', AsignacionUpdateView.as_view(), name='asignacion_update'),
    path('<int:pk>/eliminar/', AsignacionDeleteView.as_view(), name='asignacion_delete'),
    path('asignar-empleado/', asignar_empleado, name='asignar_empleado'),
]
