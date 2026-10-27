---
title: "Administrar espacios y recursos"
weight: 3
lastmod: 2026-06-12T09:50:35Z
dokuwiki: espacios_recursos
---
La sección **Administrar espacios y recursos** da acceso a crear y editar espacios y recursos de la institución.

![](/media/administrarespacioyrecursos.png?w=250&align=center)

La pantalla principal se divide en dos apartados:

- **Espacios**: pone a disposición de la plataforma salas o áreas reservables.
- **Recursos compartidos**: permite crear y modificar recursos comunes de una ubicación concreta. Quedarán disponibles para que los solicitantes los incluyan en las reservas de espacios. Se entiende que todos los recursos compartidos están disponibles para todos los espacios de una ubicación. La plataforma se ocupa de controlar la disponibilidad en cada momento.

El botón **Mostrar calendario**  muestra una vista general de la planificación de uso de los espacios y su estado.

## Añadir espacio

La información a cumplimentar es la siguiente:

![](/media/nuevoespacio.png?w=500&align=center)

- **Nombre**: una identificación del espacio.
- **Ubicación**: sede o edificio al que pertenece el espacio.
- **Capacidad**: número máximo de personas.
- **Tiempo extra antes y después (min)**: margen de tiempo adicional reservado antes y después de cada uso del espacio. A cualquier reserva del espacio se le añade ese número de minutos antes y después, con objeto de que se pueda realizar tareas de mantenimiento.
- **Dirección**: ubicación física del espacio.
- **Descripción**: información adicional relevante.
- **Activo**: permite habilitar o deshabilitar el espacio para su reserva. Si el Espacio se marca como No activo, no estará disponible para reserva hasta que se restablezca como Activo.

Es necesario **Guardar**  la descripción del espacio. A continuación, tendrás la opción de añadir Recursos propios en el espacio creado. Los Recursos propios son aquellos que están vinculados a un espacio y no se pueden compartir con otros.

![](/media/recursodeespacio.png?w=500&align=center)

Como se puede observar en la imagen anterior, podrás especificar el almacén en el que está el recurso y establecer su disponibilidad:

- **Requiere solicitud**: sirve para identificar un recurso propio de la sala, pero que requiere una solicitud específica para su uso. Habitualmente, esto se usa para recursos que requieren una actuación. Por ejemplo, una sala puede disponer de equipo de proyección que necesita que el equipo de mantenimiento lo encienda y lo configure.
- **Siempre disponible**: es un Recurso propio de un espacio que no requiere ninguna intervención para poder usarse. Por ejemplo, una mesa, una pizarra o sillas.
- **No disponible**: es un estado de Recurso propio de un espacio que, aunque existe, no funciona o temporalmente no está en su espacio. Por ejemplo, un equipo de proyección que está averiado y en espera de reparación, o una mesa que se ha llevado a barnizar y durante unos días no está en su sala.

Finalmente, los espacios creados aparecerán en el listado principal, desde donde será posible editarlos o eliminarlos.

## Añadir recurso compartido

Los Recursos compartidos no están vinculados a espacios, sino que están a disposición de los solicitantes para incluirlos en sus peticiones de reserva. Por ejemplo, un conjunto de sillas supletorias que están en un almacén y pueden transportarse e instalarse en cualquier sala. La información a cumplimentar es la siguiente:

![](/media/recursoscompartidos.png?w=500&align=center)

- **Nombre**: identificación del recurso.
- **Ubicación**: sede o edificio al que pertenece.
- **Almacén**: dónde se guarda habitualmente.
- **Unidades**: cantidad disponible, si es cuantificable.
- **Descripción**: información adicional sobre el recurso.
- **Activo**: permite habilitar o deshabilitar temporalmente el recurso. Si está Activo, el recurso queda disponible para los solicitantes. Si está No activo, no se podrá incluir en reservas de espacios. Esta funcionalidad permite que los recursos compartidos estén temporalmente en mantenimiento o cedidos a terceros.

Los recursos creados aparecerán en el listado principal, desde donde será posible editarlos o eliminarlos.

Es posible dar de alta tantos espacios y recursos como sean necesarios.
