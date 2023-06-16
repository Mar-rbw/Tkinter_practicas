# Documentar un programa
__Fuente: https://www.youtube.com/watch?v=SJqANWdRG4I__
hasta minuto: 7:27
* ¿Qué es?
    * Incluir comentarios en clases, métodos, módulos, etc.
* ¿Para qué?
    * Para ayudar en el trabajo en equipo. Especialmente útil en aplicaciones complejas

Esta bien incluir comentarios en clases,  métodos, módulos, etc 
Para explicar cada cosa.A la hora de trabajar en equipo. en aplicaciones muy complejas donde hay, cientos de clases o cientos de métodos. Es muy importante saber **para que se creo ese método** y **cual es su desempeño**, cual es la utilidad de esa clase que no hemos hecho nosotros

## Aun sino tenemos equipo

Si trabajas solo, el documentar un proyecto muy complejo,es excelente documentar esa apliación es posible que dentro de un tiempo(días, meses, incluso años) y no recuerdes nada de lo hecho. El tener una documentación de ese programa nos ayuda a recodar como funcionaba.

## Ejemplo
<pre>

   
class Areas:
   """Esta clase calcula las áreas de diferentes figuras geométicas""""

    def area_cuadrado(lado):
       """"Calcula el área de un cuadrado
    elevando al cuadrado el lado pasdado por parámetro"""
        return  f"El área del cuadrado es: {lado*lado}"
    """Calcula el area de un triangulo utilizando losparametros    base y altura"""
    def area_triangulo(base,altura):
        return "El área del triangulo es: {(base*altura)/2}"
       print(area_cuadrado(5))
    """Muestrame la documentacion asociada a'area_cuadrado'"""
    print(areaCuadrado.__doc__)

    """Suponiendo que no estan en una Class o Clase""""
    """Nos ofrece una información más detalla, 
        nos dice ayuda en la función area_cuadrada en modulo principal(main):
        * La definición de la función con sus parametros y la documentación asosiada"""
    help(area_cuadrado)
    """Nos ofrece lo mismo anterior aun sin pasar por __doc__"""
    help(areaTriangulo)

   """Si estas en una clase"""
   help(Areas.area_triangulo)
   """Para una ayuda general de la clase
      Mostrara la ayuda en la clase Areas en el modulo principal(main)
      Los metodos definidos y sus documentaciones respectivas
   """
   help(Areas)

   
   
</pre>
