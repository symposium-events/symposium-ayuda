---
title: "Cupones descuento"
weight: 2
lastmod: 2020-02-24T09:13:31Z
dokuwiki: cupones_descuento
---
Los Organizadores de eventos disponen de un sistema de cupones descuento, aplicables a las inscripciones de pago. Esta herramienta se encuentra en el menú **Asistentes > Cupones descuento.**

![](/media/admin/cupones_descuento.png?w=250&align=center)

A menudo, la organización del evento puede querer facilitar un descuento del importe de la inscripción a un grupo de asistentes. Es posible crear cupones descuento por importe fijo o que reduzcan en un porcentaje el valor de la inscripción.

**Es requisito imprescindible haber aplicado al evento una *[plantilla responsive](/docs/eventos/diseno/plantillas-responsivas)*** .

## Cupones

Cada cupón descuento contiene:

- **Nombre descriptivo**: Sirve al Organizador para identificar internamente el cupón. No puede haber dos cupones con el mismo nombre dentro del evento.
- **Código**: Un conjunto de letras mayúsculas y/o números. Es el código que usuarán los asistentes para inscribirse en el evento beneficiándose de su descuento.
- **Tickets asociados**: Cada cupón debe estar asociado, al menos, a una inscripción de pago. También puede estar asociado a más tipos de inscripción.
- **Tipo de descuento asociado**: El descuento puede ser un importe fijo, o un porcentaje.
- **Valor del cupón**: Dependiendo del tipo de descuento, se ha de especificar la cantidad o el porcentaje que se descontará de las inscripciones asociadas al cupón. No hay que poner símbolos, ni de la moneda ni del porcentaje.
- **Fecha de caducidad****:**Es posible establecer una fecha límite para la validez de cada cupón descuento. Se se deja en blanco, el cupón no caducará y podrá usarse hasta el cierre del plazo de inscripción del evento.
- **Stock**: Se puede especificar cuántos cupones hay disponibles. Si se quieren infinitos cupones, se puede poner un cero (0).

![](/media/admin/creacion_cupon.png?w=500&align=center)

## Requisitos para crear cupones descuento

1. El evento debe tener aplicada una **[plantilla responsive](/docs/eventos/diseno/plantillas-responsivas)** .
1. Se requiere la inscripción al evento en [modo](/docs/eventos/asistentes/inscripcion)**[De pago](/docs/eventos/asistentes/inscripcion).**
1. Se requiere, al menos, una **Inscripción****de pago**  y con importe mayor que cero, puesto que no es posible asignar cupones descuento a inscripciones gratuitas.

Si creas dos o más cupones descuento, todos deben tener nombres y códigos distintos. No puede haber un cupón con el mismo código que otro, pero tampoco puede haber dos con el mismo nombre.

Si una inscripción está asociada a dos o más cupones, los usuarios sólo podrán beneficiarse de uno de los descuentos.

## Aplicación de los cupones descuento

Los usuarios que dispongan de un cupón descuento podrán utilizarlo en el último paso del proceso de inscripción.

![](/media/admin/aplicacion_cupon.png?w=900&align=center)

## Stock y cancelaciones

Como Organizador, puedes comprobar cuántos cupones se han utilizado y cuántos quedan disponibles. En el caso de cupones con stock limitado, cuando un asistente cancele su inscripción, el cupón que haya utilizado regresará al stock de cupones disponibles y podrá utilizarlo otro asistente.

![](/media/admin/cupones_descuento_panel.png?w=800&align=center)

## Panel Económico

El Gestor económico puede comprobar desde su Panel qué asistentes han utilizado un cupón y el descuento aplicado. Este descuento también quedará reflejado en las facturas emitidas, cuando se utilice esa funcionalidad de Symposium.

![](/media/admin/cupon_panel_economico.png?w=833&align=center)
