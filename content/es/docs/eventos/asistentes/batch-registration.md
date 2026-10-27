---
title: "Inscripción masiva"
weight: 11
lastmod: 2020-02-17T13:18:50Z
dokuwiki: batch_registration
---
Es posible que para un Evento sea el Organizador quien deba dar de alta asistentes. Esto puede ocurrir porque estos asistentes se han localizado por otros medios distintos de la web del Evento y han confirmado su interés, pero no quieren o no pueden hacer el proceso de inscripción personalmente. Symposium ofrece una utilidad para hacer una carga masiva de asistentes a partir de un fichero del tipo Valores Separados por Comas (o CSV por sus siglas en inglés). Esta utilidad se encuentra en **Asistentes > Inscripción masiva**.

Es posible registrar a un listado de usuarios en un evento a través de un fichero CSV.

![](/media/panel_organizador/masiva.png?w=250&align=center)

## Requisitos

Para poder utilizar la inscripción masiva, es necesario tener configurada al menos una [Inscripción](/docs/eventos/asistentes/inscripcion). No es necesario que esté marcada como visible o disponible, puede estar oculta en la web del Evento, pero podrá utilizarse en esta sección.

Solamente aparecerán disponibles las inscripciones gratuitas y las de pago, siempre y cuando el pago por trasferencia bancaria esté activo para el evento. Esto es así porque el organizador esperará el ingreso del inscrito únicamente por trasferencia.

Se debe tener la lista de asistentes ya preparada para trasladarla a un fichero de tipo CSV, que es el formato que puede leer la aplicación.

## Proceso de inscripción masiva

### Utilizar una plantilla

Si bien Symposium puede leer un fichero de tipo CSV con los datos de los asistentes, los campos dentro de este deben seguir un orden determinado. Para facilitar la tarea, ya existe una [plantilla](/descargas/registration_es.csv). También se puede obtener desde el texto de ayuda del panel de Inscripción masiva. En esta plantilla, se deben sustituir los datos de ejemplo que ya contiene por los correctos, pero sin modificar el orden de las columnas.

Es posible editar el fichero con cualquiera de las muchas aplicaciones compatibles con el formato CSV. Habitualmente, se usa un software de hojas de cálculo, como [Microsoft Excel](https://products.office.com/es-es/excel), [OpenOffice Calc (gratuíto)](https://www.openoffice.org/), [LibreOffice Calc (gratuíto)](https://es.libreoffice.org/), etc. También es posible usar un editor de texto plano, pero hacerlo así aumenta la probabilidad de cometer errores.

A la hora de trabajar con texto hay varios estándares que permiten determinados caracteres de texto y no otros. Para asegurar la compatibilidad del texto en cualquier idioma, es importante asegurarse que la aplicación trabaja con el estándar UTF-8 y que guarda el fichero CSV con dicho estándar.

Si no se trabaja con UTF-8, es muy posible que las letras acentuadas, las eñes y demás símbolos que puedan ser específicos de un idioma no se guarden bien en la aplicación.

Una vez cumplimentados los datos, la plantilla se debe guardar manteniendo el formato CSV, puede utilizarse el mismo nombre de archivo que ya tiene.

### Carga del fichero de datos

Desde el panel Inscripción masiva, haz clic en el botón Seleccionar archivo para localizarlo en el ordenador donde se está haciendo el proceso y súbelo a Symposium con el botón Continuar.

Al cabo de unos segundos, aparecerá en pantalla una tabla con el contenido del fichero.

![](/media/batch_registration/batch-registration.png?align=center)

Es el momento de revisar que todos los datos están correctos y en el sitio que deben estar y no, por accidente, en otra columna que no les corresponde. Para que una fila sea correcta debe:

- existir un nombre de asistente válido en la columna de nombre
- existir apellidos válidos en la columna apellidos (el campo no puede estar vacío)
- existir un correo electrónico válido en la tercera columna (debe presentar un formato adecuado *aaa@bbb.ccc*)

Las filas correctas se colorearán con fondo verde. Las incorrectas, con fondo rojo, con un tono más intenso en la celda que contiene el error.

En el ejemplo de la imagen de arriba se observa un error frecuente. En la primera fila del área que debiera contener daros de asistentes se ha duplicado la fila de títulos y, aunque en las columnas Nombre y Apellidos hay texto válido (Symposium no puede saber si realmente hay un nombre y unos apellidos, sólo si hay texto), en la columna Correo electrónico no hay una dirección de email válida, sino la cadena de texto "Correo electrónico", que no cumple el requisito de formato que suelen tener las direcciones de email.

**MUY IMPORTANTE**: se debe comprobar que los caracteres especiales (acentos, eñes…) se muestran correctamente. Si no es así, se deberá editar de nuevo el listado de asistentes en la plantilla CSV con el software que se haya usado y al guardar marcar la opción Codificación (Encoding) UTF-8. Si el software que se está usando no lo permite, deberá utilizarse otro que sí lo haga.

### Selección de asistentes

En cada fila habrá un cuadro tipo check para marcar los asistentes que se desean incorporar al Evento. Esto existe por que es posible que del listado se quiera descartar a alguno o a algunos. Las filas que contengan errores no se pueden seleccionar.

Se puede seleccionar todo el listado (menos las filas erróneas) o quitar la selección a todos haciendo clic en el mismo cuadro check que hay en la fila de cabecera de la tabla.

A continuación, de la lista deplegable Inscribir asistentes se debe escoger la Inscripción a la que se va a asignar a todo el listado de asistentes, hacer clic en el botón Inscribir asistentes (que además indica cuántos se van a agregar al Evento) y aguardar unos segundos al mensaje Operación completada.

### Revisar y corregir

A continuación, lo prudente es revisar el menú **Asistentes > Listado de Asistentes**  para comprobar que las inscripciones se han grabado correctamente.

Si se ha producido algún error o falta algún inscrito, se puede repetir el proceso mediante una plantilla CSV sólo con los asistentes fallidos siguiendo los pasos anteriores.

## Ejemplos prácticos de uso de la Inscripción masiva

### Inscripción gestionada para VIPs

En el caso de que la organización de un evento desee inscribir a un grupo de VIPs ahorrándole la molestia de la tarea de la inscripción, puede utilizar esta herramienta a tal efecto.

Si se quiere evitar que el invitado reciba comunicaciones por correo electrónico, puede marcarse la opción para que los inscritos **no reciban correos electrónicos**  de su inscripción. Además, es necesario que, para poder tramitar estas inscripciones, el organizador cuente con la autorización de los usuarios a los que pretende inscribir y lo refleje aceptando los **consentimientos de la Política de Privacidad**.

![](/media/panel_organizador/masiva_lopd.png?w=667&align=center)

A continuación, el Organizador puede cumplimentar los [Formularios de inscripción](/docs/eventos/asistentes/formulario-de-inscripcion) correspondientes (en caso de haberlos) en el [Listado de asistentes](/docs/eventos/asistentes/listado).
