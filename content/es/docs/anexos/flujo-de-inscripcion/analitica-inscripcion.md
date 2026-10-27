---
title: "Analítica de inscripciones"
weight: 8
lastmod: 2021-01-13T16:26:27Z
dokuwiki: analitica_inscripcion
---
La plataforma Symposium habilita una serie de métodos Javascript que facilitan la captura de datos para su análisis. Estos datos pueden después remitirse a herramientas como Google Analytics para mantener un seguimiento de la información relativa a la inscripción a eventos y su rendimiento.

Existen 4 posibles *callbacks *a los que es posible suscribirse para recibir información relativa:

| Callback | Respuesta |
|---|---|
| `tickets_selected` |  |

```
{
event_id: 1234,
tickets_selected: [
   {
       id: 123,
       name: 'Inscripción',
       price: 10.50,
       amount: 1
   }
]
}
```

| |
|---|
|  |
| `products_selected` |

```
{
event_id: 1234,
products_selected: [
   {
     id: 123,
     name: 'Cena de gala',
     price: 50,
     amount: 2
   }
]
}
```

| |
|---|
|  |
| `pre_purchase` |

```
{
event_id: 1234,
pre_purchase: {
   tickets_selected: [
       {
          id: 123,
          name: 'Inscripción',
          price: 10.50,
          amount: 1
       }
   ],
   products_selected: [
      {
         id: 123,
         name: 'Cena de gala',
         price: 50,
         amount: 2
      }
   ],
   total: 110.50
}
}
```

| |
|---|
|  |
| `post_purchase` |

```
{
event_id: 1234,
post_purchase: {
   tickets_selected: [
       {
          id: 123,
          name: 'Inscripción',
          price: 10.50,
          amount: 1
       }
   ],
   products_selected: [
      {
         id: 123,
         name: 'Cena de gala',
         price: 50,
         amount: 2
      }
   ],
   total: 110.50
}
}
```
<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> |

Ejemplo de suscripción a uno de los callback:

```
SYMJS.addCallback('tickets_selected', function (data) {
    // Tu código
});
```

Este código se puede insertar de tres maneras:

- Creando una plantilla personalizada lo que permite añadir scripts Javascript libremente
- Utilizando la herramienta [Personalizar](/docs/eventos/diseno/imagen-de-cabecera#incluir-html-en-la-plantilla) para poder incorporar código al evento
- Utilizando una herramienta de inserción de código como Tag Manager de Google

Ejemplo de inserción de código utilizando la herramienta [Personalizar](/docs/eventos/diseno/imagen-de-cabecera#incluir-html-en-la-plantilla) para incrustar un script Javascript y enviar los datos a través de Tag Manager a Google Analytics:

```
<script type="text/javascript">
(function() {
var waitJSReady = setInterval(function(){
    if(typeof SYMJS.addCallback != 'undefined') {
        clearInterval(waitJSReady);

        SYMJS.addCallback('tickets_selected', function (data) {
            var products = [];
            for (var i = 0; i <data.tickets_selected.length; i++) {
                var element = data.tickets_selected[i];
                products.push({
                    'id': 'T' + element.id,
                    'name': element.name,
                    'category': 'Inscripción',
                    'price': element.price,
                    'quantity': element.amount
                });
            }
            dataLayer.push({
                'event': 'EEaddToCart',
                'ecommerce': {
                    'add': {
                        'actionField': {
                            'affiliation': data.event_id
                        },
                        'products': products
                    }
                }
            });
        });

        SYMJS.addCallback('products_selected', function (data) {
            var products = [];
            for (var i = 0; i <data.products_selected.length; i++) {
                var element = data.products_selected[i];
                products.push({
                    'id': 'P' + element.id,
                    'name': element.name,
                    'category': 'Producto',
                    'price': element.price,
                    'quantity': element.amount
                });
            }
            dataLayer.push({
                'event': 'EEaddToCart',
                'ecommerce': {
                    'add': {
                        'actionField': {
                            'affiliation': data.event_id
                        },
                        'products': products
                    }
                }
            });
        });

        SYMJS.addCallback('pre_purchase', function (data) {
            var products = [];
            for (var i = 0; i <data.pre_purchase.tickets_selected.length; i++) {
                var element = data.pre_purchase.tickets_selected[i];
                products.push({
                    'id': 'T' + element.id,
                    'name': element.name,
                    'category': 'Inscripción',
                    'price': element.price,
                    'quantity': element.amount
                });
            }
            for (var j = 0; j <data.pre_purchase.products_selected.length; j++) {
                var element = data.pre_purchase.products_selected[j];
                products.push({
                    'id': 'P' + element.id,
                    'name': element.name,
                    'category': 'Producto',
                    'price': element.price,
                    'quantity': element.amount
                });
            }
            dataLayer.push({
                'event': 'EEcheckout',
                'ecommerce': {
                    'checkout': {
                        'actionField': {
                            'affiliation': data.event_id
                        },
                        'products': products
                    }
                }
            });
        });

        SYMJS.addCallback('post_purchase', function (data) {
            var products = [];
            for (var i = 0; i <data.post_purchase.tickets_selected.length; i++) {
                var element = data.post_purchase.tickets_selected[i];
                products.push({
                    'id': 'T' + element.id,
                    'name': element.name,
                    'category': 'Inscripción',
                    'price': element.price,
                    'quantity': element.amount
                });
            }
            for (var j = 0; j <data.post_purchase.products_selected.length; j++) {
                var element = data.post_purchase.products_selected[j];
                products.push({
                    'id': 'P' + element.id,
                    'name': element.name,
                    'category': 'Producto',
                    'price': element.price,
                    'quantity': element.amount
                });
            }
            dataLayer.push({
                'event': 'EEtransaction',
                'ecommerce': {
                    'purchase': {
                        'actionField': {
                            'id': data.post_purchase.invoice,
                            'affiliation': data.event_id,
                            'revenue': data.post_purchase.total
                        },
                        'products': products
                    }
                }
            });
        });

    }
}, 500);
})();
</script>
```
