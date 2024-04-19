AREA_OPERATIVA = (
    (0, 'Dirección General'),
    (1, 'Finanzas'),
    (2, 'Ventas'),
)
ESCOLARIDAD = (
    (0, 'Primaria'),
    (1, 'Secundaria'),
    (2, 'Preparatoria'),
    (3, 'Carrera técnica'),
    (4, 'Diplomado'),
    (5, 'Licenciatura'),
    (6, 'Posgrado'),
    (7, 'Doctorado'),
)
ESTADO_CIVIL = (
    (0, 'Soltero'),
    (1, 'Casado'),
    (2, 'Unión libre'),
    (3, 'Divorciado'),
)
ESTADOS = (
    (0, 'Sin Estado'),
    (1, 'Aguascalientes'),(2, 'Baja California'),(3, 'Baja California Sur'),
    (4, 'Campeche'),(5, 'Coahuila'),(6, 'Colima'),(7, 'Chiapas'),(8, 'Chihuahua'),
    (9, 'Ciudad de México'),(10, 'Durango'),(11, 'Guanajuato'),(12, 'Guerrero'),
    (13, 'Hidalgo'),(14, 'Jalisco'),(15, 'México'),(16, 'Michoacán'),(17, 'Morelos'),
    (18, 'Nayarit'),(19, 'Nuevo León'),(20, 'Oaxaca'),(21, 'Puebla'),(22, 'Querétaro'),
    (23, 'Quintana Roo'),(24, 'San Luis Potosí'),(25, 'Sinaloa'),(26, 'Sonora'),
    (27, 'Tabasco'),(28, 'Tamaulipas'),(29, 'Tlaxcala'),(30, 'Veracruz'),(31, 'Yucatán'),
    (32, 'Zacatecas'),
)
ESTATUS_ARMAMENTO = (
    (0, 'Asignado'),
    (1, 'Baja'),
    (2, 'Sin Asignar'),
    (3, 'Taller'),
    (99, 'Otro'),
)
ESTATUS_BAJA_ACTIVO = (
    (0, 'Baja'),
    (1, 'Activo'),
)
ESTATUS_EMPLEADO = (
    (0, 'Asignado'),
    (1, 'Baja'),
    (2, 'Sin Asignar'),
    (3, 'Suspendido'),
    (99, 'Otro'),
)
ESTATUS_EVENTO_ASIG = (
    (0, 'Cancelado'),
    (1, 'En curso'),
    (2, 'Terminado'),
)
ESTATUS_SERVICIO = (
    (0, 'Baja'),
    (1, 'Cancelado'),
    (2, 'En curso'),
    (3, 'En revisión'),
    (4, 'Nuevo'),
    (5, 'Suspendido'),
    (6, 'Terminado'),
)
ESTATUS_VEHICULO = (
    (0, 'Asignado'),
    (1, 'Baja'),
    (2, 'Sin Asignar'),
    (3, 'Taller'),
    (99, 'Otro'),
)
FAMILIAR = (
    (0, 'Conyuge'),
    (1, 'Hijo'),
    (2, 'Padre'),
    (3, 'Madre'),
    (4, 'Conocido'),
)
GENERO = (
    (0, 'Masculino'),
    (1, 'Femenino'),
)
IDIOMA = (
    (0, 'Español'),
    (1, 'Inglés'),
    (2, 'Francés'),
    (3, 'Italiano'),
    (4, 'Ruso'),
    (5, 'Chino'),
    (6, 'Coreano'),
    (7, 'Otro'),
)
MARCA_ARMAMENTO = (
    (1, 'Beretta'),
    (2, 'Browning'),
    (3, 'Colt'),
    (4, 'CZ (Česká zbrojovka)'),
    (5, 'FN Herstal'),
    (6, 'Glock'),
    (7, 'Heckler & Koch (H&K)'),
    (8, 'Mossberg'),
    (9, 'Remington'),
    (10, 'Ruger'),
    (11, 'SIG Sauer'),
    (12, 'Smith & Wesson'),
    (13, 'Springfield Armory'),
    (14, 'Taurus'),
    (15, 'Winchester'),
    (99, 'Otra'),
)
MARCA_VEHICULO = (
    (1, 'Audi'),
    (2, 'BMW'),
    (3, 'Chevrolet'),
    (4, 'Ford'),
    (5, 'Honda'),
    (6, 'Hyundai'),
    (7, 'Kia'),
    (8, 'Lexus'),
    (9, 'Mazda'),
    (10, 'Mercedes-Benz'),
    (11, 'Nissan'),
    (12, 'Subaru'),
    (13, 'Tesla'),
    (14, 'Toyota'),
    (15, 'Volkswagen'),
    (99, 'Otra'),
)
PAGO = (
    (0, 'Horas'),
    (1, 'Diario'),
    (2, 'Semanal'),
    (3, 'Quincenal'),
    (4, 'Mensual'),
)
SI_NO = (
    (0, 'NO'),
    (1, 'SI'),
)
TIPO_ARMAMENTO = (
    (1, 'Ametralladora ligera'),
    (2, 'Ametralladora pesada'),
    (3, 'Escopeta'),
    (4, 'Fusil de asalto'),
    (5, 'Pistola'),
    (6, 'Revólver'),
    (99, 'Otro'),
)
TIPO_CALIBRE = (
    (1, '12 Gauge (Calibre 12)'),
    (2, '20 Gauge (Calibre 20)'),
    (3, '.357 Magnum (9x33mmR)'),
    (4, '.38 Special (9x29mmR)'),
    (5, '.380 ACP (9x17mm)'),
    (6, '.44 Magnum (10.9x33mmR)'),
    (7, '.45 ACP (11.43x23mm)'),
    (8, '5.56x45mm NATO (.223 Remington)'),
    (9, '7.62x51mm NATO (.308 Winchester)'),
    (10, '9mm Parabellum (9x19mm)'),
    (99, 'Otro'),
)
TIPO_COMBUSTIBLE = (
    (1, 'Diésel'),
    (2, 'Gas LP'),
    (3, 'Gasolina Magna (Regular)'),
    (4, 'Gasolina Premium'),
    (5, 'Eléctrico'),
    (99, 'Otro'),
)
TIPO_EMPLEADO = (
    (0, 'Interno'),
    (1, 'Externo'),
)
TIPO_EVENTO_ASIGANCION = (
    (0, 'Suspensión'),
    (1, 'Incidente'),
    (2, 'Comentario'),
    (3, 'Otro'),
)
TIPO_PERSONA = (
    (0, 'Física'),
    (1, 'Moral'),
)
TIPO_REFERENCIA = (
    (0, 'Personal'),
    (1, 'Empresa'),
)
TIPO_SERVICIO = (
    (0, 'Sin servicio'),
    (1, 'Escolta mixta'),
    (2, 'Escolta personal'),
    (3, 'Escolta vehicular'),
    (4, 'Monitoreo'),
    (5, 'Seguridad en evento'),
    (6, 'Traslado de valores'),
    (7, 'Vigilancia en bienes muebles'),
    (99, 'Otro'),
)
TIPO_VEHICULO = (
    (1, 'Autobús'),
    (2, 'Automóvil'),
    (3, 'Bicicleta'),
    (4, 'Camión'),
    (5, 'Camioneta'),
    (6, 'Furgoneta'),
    (7, 'Motocicleta'),
    (8, 'RV (Vehículo recreativo)'),
    (9, 'SUV (Vehículo utilitario deportivo)'),
    (99, 'Otro'),
)
