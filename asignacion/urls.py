from django.urls import path
from .views import AsignacionListView, AsignacionCreateView, AsignacionUpdateView, \
    AsignacionDeleteView, asignar_empleado, AsignacionAutoriza, AsignacionSuspende, \
    AsignacionEvento

urlpatterns = [
    path('asignaciones/', AsignacionListView.as_view(), name='asignacion_list'),
    path('crear/', AsignacionCreateView.as_view(), name='asignacion_create'),
    path('<int:pk>/editar/', AsignacionUpdateView.as_view(), name='asignacion_update'),
    path('<int:pk>/eliminar/', AsignacionDeleteView.as_view(), name='asignacion_delete'),
    path('asignar-empleado/', asignar_empleado, name='asignar_empleado'),
    path('autoriza/<int:pk>/', AsignacionAutoriza.as_view(), name='asignacion_autoriza'),
    path('elimina/<int:pk>/', AsignacionDeleteView.as_view(), name='asignacion_elimina'),
    path('suspende/<int:pk>/', AsignacionSuspende.as_view(), name='asignacion_suspende'),
    path('evento/<int:pk>/', AsignacionEvento.as_view(), name='asignacion_evento'),
]
