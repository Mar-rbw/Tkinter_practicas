# Ventanas utilizando POO

## Frame

Los Frames son **marcos contendores de otros widgets**. Pueden tener tamaño propio y **posicionarse en distintos lugares de otro contenedor**(ya qsea ka raíz y **otro marco**)

Elemento relacionado en Entorno_6.py


## Frame(Configuración)

w = Frame ( master, option, ...)

```python
    w.config(bg="blue")  # color de fondo, background
    w.config(curso="pirate") # tipo de cursor (arrow defecto)
    w.confgi(relief="sinken") # relieve del frame
    w.config(bd=25) # tamaño del borde en pixeles
```

| Efecto                   |                                   Sintaxis |
| :----------------------- | -----------------------------------------: |
| Cambiar el tamaño        | mi_Frame.config(width="400", height="200") |
| Cambiar color de fondo   |                 mi_Frame.config(bg="blue") |
| Cambiar grosor del borde |                     mi_Frame.config(bd=24) |
| Cambiar el tipo de borde |           mi_Frame.config(relief="sunken") |
| Cambiar el cursor        |            mi_Frame.config(cursor="heart") |

Referencia de elementos en Entorno_6.py

## Ventajas de utilizar POO

Revisar elementos en entorno_8.py
