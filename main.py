# main.py
from libros import Libro, Usuario, Prestamo, Biblioteca
from datetime import date
from decimal import Decimal

# Crear libros
libro1 = Libro(codigo="001", titulo="Python para todos", autor="Juan Pérez", fecha_publicacion=date(2020, 5, 1), precio=Decimal('25.99'))
libro2 = Libro(codigo="002", titulo="Data Science con Python", autor="Ana García", fecha_publicacion=date(2021, 3, 15), precio=Decimal('30.50'))
libro3 = Libro(codigo="003", titulo="Ciencia de Datos con Python", autor="Carlos Díaz", fecha_publicacion=date(2021, 11, 1), precio=Decimal('45.99'))
libro4 = Libro(codigo="004", titulo="Aprende JavaScript", autor="Marta Gómez", fecha_publicacion=date(2020, 9, 15), precio=Decimal('35.75'))
libro5 = Libro(codigo="005", titulo="Desarrollo Web", autor="Luis Fernández", fecha_publicacion=date(2022, 3, 22), precio=Decimal('50.00'))
libro6 = Libro(codigo="006", titulo="Introducción a la IA", autor="Sandra Ruiz", fecha_publicacion=date(2019, 7, 10), precio=Decimal('40.00'))

# Crear usuario
usuario1 = Usuario(dni="12345678", nombre="Carlos López", fecha_nacimiento=date(1990, 7, 20))
usuario2 = Usuario(dni="23456789", nombre="Lucía Martínez", fecha_nacimiento=date(1995, 5, 15))
usuario3 = Usuario(dni="34567890", nombre="Pedro Rodríguez", fecha_nacimiento=date(1988, 12, 30))

# Crear préstamo
prestamo1 = Prestamo(libro=libro1, usuario=usuario1, fecha_prestamo=date.today())
prestamo2 = Prestamo(libro=libro3, usuario=usuario2, fecha_prestamo=date.today())
prestamo3 = Prestamo(libro=libro4, usuario=usuario3, fecha_prestamo=date.today())

# Crear biblioteca y agregar elementos
biblioteca = Biblioteca()
biblioteca.agregar_elemento(libro1)
biblioteca.agregar_elemento(libro2)
biblioteca.agregar_elemento(libro3)
biblioteca.agregar_elemento(libro4)
biblioteca.agregar_elemento(libro5)
biblioteca.agregar_elemento(libro6)
biblioteca.agregar_elemento(usuario1)
biblioteca.agregar_elemento(usuario2)
biblioteca.agregar_elemento(usuario3)
biblioteca.agregar_elemento(prestamo1)
biblioteca.agregar_elemento(prestamo2)
biblioteca.agregar_elemento(prestamo3)

# Imprimir descripción de todos los elementos en la biblioteca
print("Elementos en la biblioteca:")
for descripcion in biblioteca.listar_elementos():
    print(descripcion)

# Mostrar detalles de los préstamos
print("\nDetalles del préstamo 1:")
print(prestamo1.mostrar_detalles())

print("\nDetalles del préstamo 2:")
print(prestamo2.mostrar_detalles())

print("\nDetalles del préstamo 3:")
print(prestamo3.mostrar_detalles())