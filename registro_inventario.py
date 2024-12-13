"""
REGISTRO DINÁMICO DE INVENTARIO
Una tienda necesita registrar su inventario de productos. Cada producto debe incluir el nombre, precio y cantidad en stock. Los datos se almacenarán en una tupla anidada.

INTRUCCIONES
1) Crea un programa que permita al usuario agregar productos al inventario.
2) Cada producto se representará como una tupla (nombre, precio, cantidad).
El programa debe preguntar al usuario si desea agregar más productos. Si responde "no", debe salir de la interacción y mostrar el inventario actual.
4) Usa un bucle para permitir el ingreso dinámico de productos y almacénalos en una tupla.
"""

# Comienza con una tupla vacía, que luego va a almacenar los productos agregados
INVENTARIO = ()

# Defino una función para agregar un nuevo producto, que tendrá varios argumentos (nombre, precio y cantidad en stock)
def agregar_producto():
    nombre = input("\nIngrese el producto que desea agregar: ").capitalize()
    precio = float(input(f"Ingrese el precio para el producto «{nombre}»: $"))
    cantidad = int(input(f"Ingrese la cantidad en stock para «{nombre}»: "))
    
    # Tupla que contiene el valor de los argumentos
    producto = (nombre, precio, cantidad)
    
    # Función «global» modifica la variable INVENTARIO fuera de la función «agregar_producto()» y no crea otra variable del mismo nombre para almacenar los argumentos ingresados
    global INVENTARIO
    INVENTARIO += (producto, ) # += para agregar la tupla «producto» a la tupla INVENTARIO
    
while True:
    agregar_producto()
    mas_productos = input("\n¿Desea seguir agregando más productos al inventario? (Sí/No): ").strip().capitalize()
    
    if mas_productos == "No":
        break

# Muestro el inventario con los productos agregados previamente
print("El inventario hasta la fecha es: ")
for producto in INVENTARIO:
    nombre, precio, cantidad = producto
    print(f"{nombre} - Precio: ${precio:.2f} - Stock: {cantidad}")