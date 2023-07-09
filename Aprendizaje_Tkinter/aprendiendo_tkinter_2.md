# Posicionar controles dentro de una ventana

## Gestores de geometría

Definir el *modo en que deben colocarse los widgets*(Controles) dentro de una ventana:

    - place
    - pack
    - grid 

Para construir la ventanas se pueden utilizar unos widgets especiales (*marcos, paneles, etc.*) que *actúan como contenedores* de otros widgets. Estos widgets se utilizan para agrupar varios controles.

*No deben mezclarse distintos métodos* dentro de un mismo contenedor

## Posición absoluta

### Place

Permite ubicar elementos indicando su posición (X e Y) respecto de un elemento padre

self.button.place (x=60 y=40, width=100, height=30)

X = Separación de la ventana desde Lado izquierdo
Y = Separacion de la ventana desde Arriba
width = El ancho
height = altura

Valores **ABSOLUTOS**

self.button.place (relx=0.1 rely=0.1, relwidth=0.5, relheight=0.5)

se traducen 10%,10%,50%,50%

Valores **relativos al padre (contenedor)**

Estos valores aceptan valores entre 0 y 1

Contenido de la relacionado: Entorno_3.py.

```python
    """ Para cambiar la resolución a relativo se debe usar
        la siguiente ecuación:
            relx = x / ancho_de_ventana
            rely = y / altura_de_ventana

            Ejemeplo:
                El valor de "x" es 400 (ancho de la ventana).
                El valor de "y" es 200 (altura de la ventana).
             """
                relx = x / 400
                rely = y / 200
            

```

## Posicionamiento relativo

### Pack

En lugarde especificar las coordenadas de un elemento, simplemente le decimos que debe ir arriba, abajo, a la izquierda o a la derecha respecto de algún contenedor.

Si no indicamos ningún argumento, por defecto Tk posicionará los elementos uno arriba del otro.

```python
    entry = ttk.Entry(self)
    entry.pack()

    button = ttk.Button(self, text="Hola, mundo!")
    button.pack()
```

La propiedad que controla la posición relativa de los elementos es **side**, que puede equivaler a **tk.TOP**(por defecto), **tk.BOTTOM**,**tk.LEFT** O **tk.RIGHT**. De este modo, si indicamos que la caja de texto debe ir ubicada a la izquierda, los otros dos controles se seguirán manteniendo uno arriba del otro.
```Python
    self.entry = ttk.Entry(self)
    self.entry.pack(side=tk.LEFT)
```

También admite los parámetros  **after y before**, que nos permiten controlar el orden en el que se ubican los elementos en la ventan. El siguiente ejemplo obliga a Tk a colocar la etiqueta  **self.label antes(before) que la caja de texto**.

```python
    self.entry = ttk.Entry(self)
    self.entry.pack()

    self.button = ttk.Button(self, text="Hola mundo!")
    self.button.pack()

    #Esta caja sera asigna antes de la caja de texto
    self.label = ttk.Label(self, text="... desde Tkinter")
    self.label.pack(before=self.entry)
```

**padx,ipadx,pady y ipady**

Especifican (en píxeles) los margenes externos e internos de un elemento

padx y pady = Margenes externos del elemento(O sea por fuera)
ipadx y ipady = Margenes internos del elemento(O sea por dentro)

```python
    def __init__(slef, main_window):
        super().__init__(main_window)
        main_window.title("Posicionar elementos en Tcl/Tk")

        self.Button = ttk.Button(self, text="Hola, mundo!")
        self.button.pack(padx=30, pady=30, ipadx=30, ipady=80)

        self.pack()
```

Se expande si la venta se expande, sie cambia de tamaño
**expand** True/False
Se expande de forma horizontal o vertical.
**fill** tk.BOTH, tk.X(horizontal), tk.Y(Vertical)

Especifican qué elementos deben expandirse o contraerse a medida que el tamaño de la ventana cambia, y en qué sentido deben hacerlo (vertical u horizontal)

```python
    self.button = ttk.Botton(self, text="Hola mundo!")
    self.button.pack(expand=True, fill=tk.X)

    self.pack(expand=True, fill=tk.Both)
```

Contenido relacionado Entorno_4.py

## Manejo en forma de grilla
### Grid

Consiste en dividir conceptualmente la ventana principal en filas (rows) y columnas (columns), formando celdas en donde se ubican los elementos

```python
    self.entry = ttk.Entry(self)
    self.entry.grid(row=0,column=0)

    self.button = ttk.Button(self, text="Presione aqui")
    self.button.grid(row=0, column=1)

    self.label = ttk.label(self, text="Hola mundo")
    self.label.grid(row=1, column=0)
    
    self.grid(sticky="nsew)

```

**columnspan, rowspan**: Indica cuántas columnas o filas debe ocupar el control (por defecto 1)

```python
    self.label.grid(row=1, colmn=0, columnspan=2)
```

**rowconfigure, columnconfigure**: Con el parámetro weight=1 indicamos que la fila o columna se expanden o contraen si la ventana cambia su tamaño.

```python
    #Expandir horizontalment a columna 0
    self.comumnconfigure(0, weight=1)
    #Expandir verticalmente la fila 0
    self.rowconfigure(0, weight=1)
```

**sticky**
Para que  un control se posicione arriba, abajo, a la derecha o izquierda de la celda que lo contiene, se usa sticky con las opciones: "n"(norte), "s"(sur),"e"(este),"w"(oeste).

```python
    #Anclar en la parte superior (n) de la celda
    self.entry.grid(row=0, column=0, sticky="n")
```

También permite que el widget se expanda de forma horizontal ("ew), vertical("ns) o en ambas direcciones("nsew")

```python
#Expandor en todas las direcciones.
self.entry.grid(row=0, column=0, sticky="nsew")
```

**rowconfigure, columnconfigure:**
```python
    self.label1= tk.label(
        self, text= "hola mundo", bg="#FFA500")
    self.label1.grid(row=0, column=0, sticky="new)

    self.label2= tk.label(
        self, text= "hola mundo", bg="#1E90FF")
    self.label2.grid(row=0, column=0, sticky="new)

    self.grid(sticky="nsew")

    self.columnconfigure(0, weight=1)
    self.rowconfigure(0, weight=1)
    self.rowconfigure(1, weight=1)

"""     Otro ejemplo
    self.rowconfigure(0, weight=5)
    self.rowconfigure(1, weight=1) """

```

Contenido relacionado esta en Entorno_5.py