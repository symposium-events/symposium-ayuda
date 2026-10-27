---
title: "Formularios personalizados"
weight: 8
lastmod: 2024-04-01T09:39:11Z
dokuwiki: formularios_personalizados
---
SYMPOSIUM permite crear formularios de inscripción personalizados a los administradores de plataforma. Además, puedes elegir uno de ellos como formulario por defecto para todas las inscripciones o entradas que los organizadores ofrezcan a los asistentes.

Desde **Administración**> **Configuración**> **Formularios personalizados**, tienes que hacer clic en **Nuevo formulario** para crear uno:

![](/media/archivos_asistentes/custom_form1.png?w=700&align=center)

Los tipos de preguntas disponibles son:

- Nombre completo.
- Nombre.
- Apellidos.
- Identificador fiscal.
- Teléfono.
- email.
- Dirección completa.
- Fecha de nacimiento.
- País.
- Código postal.
- Lugar.
- Otro: para permitir una mayor personalización, en esta pregunta puedes elegir el tipo de campo (texto corto, texto largo, Sí/No, selección simple, múltiple, fecha, fichero adjunto, selección de país o texto de ayuda).

En todos ellos, tienes que indicar el texto de la pregunta y una etiqueta personalizada o tag que facilite la recuperación de información:<br> ![](/media/archivos_asistentes/custom_form2.png?w=500&align=center)Antes de **Guardar**cada campo, deberás decidir si activar o no cuatro opciones:

- Obligatorio: al activar esta opción, la respuesta a esta pregunta será obligatoria.
- Ocultar: al activar esta opción, la pregunta no se mostrará al usuario.
- Público: al activar esta opción, la respuesta a esta pregunta será pública.
- Editable: al activar esta opción, permitirás que el gestor del evento pueda ocultar la pregunta al usuario.

Tras crear un formulario de inscripción personalizado, podrás editarlo o eliminarlo.

## Cómo influye esta funcionalidad en los organizadores

Una vez elijas un formulario de inscripción por defecto, este se vinculará automática e inmediatamente a todas las inscripciones que los organizadores ofrezcan a los asistentes, ya sean gratuitas o de pago. Sin embargo, **no se aplica en entradas ya existentes**.

Desde **Asistentes > [Formularios de inscripción](/docs/eventos/asistentes/formulario-de-inscripcion)** , los organizadores pueden modificar el orden de los campos. También añadir nuevos y copiar los predefinidos, así como ocultar del proceso de inscripción los campos que los administradores hayan configurado como editables.

Sin embargo, los organizadores no pueden editar ni eliminar los campos por defecto. Tampoco evitar que una entrada a su evento utilice el formulario de inscripción estándar. En caso de estar interesados en cualquiera de estas situaciones deberán solicitarlas a los administradores, que podréis llevar a cabo las peticiones desde **Administración > Configuración > Formularios personalizados**. Por ejemplo, desmarcando la condición de formulario por defecto.

| |
|---|
| <br><br>**¡ATENCIÓN!** **Cualquier configuración llevada a cabo en el menú de Formularios personalizados se aplicará automática e inmediatamente en inscripciones nuevas, pero no en las ya existentes.**<br><br> |

No obstante, la organización puede optar por eliminar la entrada existente para crearla otra vez, siempre y cuando no cuente con inscritos.

## Cómo obtener respuestas al formulario con API ATTENDEES

Puedes revisar todas las respuestas al formulario de inscripción desde el [Listado de asistentes](/docs/eventos/asistentes/listado).

Además, con la intención de facilitar la integración de información en aplicaciones externas de gestión, SYMPOSIUM permite a los administradores relacionar cada campo del formulario con una etiqueta personalizada o tag, como hemos indicado anteriormente.

Esto posibilita que, utilizando API ATTENDEES desde [nuestro portal para desarrolladores](https://apiportal.symposium.events), podáis obtener las respuestas que cada uno de los inscritos ha proporcionado durante el proceso de inscripción.

En caso de que el servicio de API ATTENDEES esté incluido en la licencia de tu institución, encontrarás su API Key en **Administración > Herramientas > [API Keys](/docs/administracion/herramientas/api-keys)**.
