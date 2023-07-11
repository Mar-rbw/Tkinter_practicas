import tkinter as tk
import mysql.connector

# Definir el objeto DAO para interactuar con la base de datos
class ProductDAO:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None
        
    def connect(self):
        self.conn = mysql.connector.connect(
            """ inserte datos de su base de datos """
            host="",
            user="",
            password="",
            database=""
        )
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                price DECIMAL(10, 2)
            )
        ''')
        self.conn.commit()

    def insert_product(self, name, price):
        query = 'INSERT INTO products (name, price) VALUES (%s, %s)'
        values = (name, price)
        self.cursor.execute(query, values)
        self.conn.commit()

    def get_all_products(self):
        self.cursor.execute('SELECT * FROM products')
        return self.cursor.fetchall()

# Definir la aplicación tkinter
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejemplo de Tkinter con Base de Datos")
        self.dao = ProductDAO()
        self.dao.connect()

        self.create_widgets()

    def create_widgets(self):
        # Etiquetas y campos de entrada
        tk.Label(self.root, text="Nombre del producto:").grid(row=0, column=0, sticky=tk.W)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Precio:").grid(row=1, column=0, sticky=tk.W)
        self.price_entry = tk.Entry(self.root)
        self.price_entry.grid(row=1, column=1)

        # Botón para agregar un producto
        self.add_button = tk.Button(self.root, text="Agregar producto", command=self.add_product)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Cuadro de texto para mostrar los productos
        self.products_text = tk.Text(self.root, width=40, height=10)
        self.products_text.grid(row=3, column=0, columnspan=2)

        # Configurar la tabla en la base de datos
        self.dao.create_table()

        # Cargar y mostrar los productos existentes
        self.load_products()

    def add_product(self):
        name = self.name_entry.get()
        price = float(self.price_entry.get())
        self.dao.insert_product(name, price)
        self.load_products()
        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

    def load_products(self):
        products = self.dao.get_all_products()
        self.products_text.delete('1.0', tk.END)
        for product in products:
            self.products_text.insert(tk.END, f"ID: {product[0]}, Nombre: {product[1]}, Precio: {product[2]}\n")

# Crear la ventana principal de tkinter y ejecutar la aplicación
root = tk.Tk()
app = App(root)
root.mainloop()
