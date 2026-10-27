---
title: "Registration analytics"
weight: 8
lastmod: 2021-01-13T16:26:27Z
dokuwiki: analitica_inscripcion
---
The Symposium platform provides a set of JavaScript methods that make it easy to capture data for analysis. This data can then be sent to tools such as Google Analytics to keep track of information about event registration and its performance.

There are 4 possible *callbacks* you can subscribe to in order to receive the related information:

| Callback | Response |
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

Example of subscribing to one of the callbacks:

```
SYMJS.addCallback('tickets_selected', function (data) {
    // Your code
});
```

This code can be inserted in three ways:

- By creating a custom template, which allows you to add JavaScript scripts freely
- By using the [Customize](/docs/eventos/diseno/imagen-de-cabecera#incluir-html-en-la-plantilla) tool to add code to the event
- By using a code injection tool such as Google Tag Manager

Example of code insertion using the [Customize](/docs/eventos/diseno/imagen-de-cabecera#incluir-html-en-la-plantilla) tool to embed a JavaScript script and send the data through Tag Manager to Google Analytics:

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
