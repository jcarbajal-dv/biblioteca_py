from abc import ABC, abstractmethod
from datetime import date
from decimal import Decimal
from typing import Optional, List

class ElementoBiblioteca(ABC):
    """Clase base abstracta para los elementos de la biblioteca."""

    @abstractmethod
    def descripcion(self) -> str:
        """Método abstracto para describir el elemento. 
        Debe ser implementado por todas las clases hijas."""
        pass
    
    @abstractmethod
    def obtener_id(self) -> str:
        """Método abstracto para obtener el identificador único del elemento 
        (como el código del libro o el DNI del usuario)."""
        pass
    
    @abstractmethod
    def mostrar_detalles(self) -> str:
        """Método abstracto para mostrar los detalles específicos del elemento."""
        pass


class Libro(ElementoBiblioteca):
    def __init__(self, codigo: str, titulo: str, autor: str, fecha_publicacion: date, precio: Decimal):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__autor = autor
        self.__fecha_publicacion = fecha_publicacion
        self.__precio = precio
    
    @property
    def codigo(self) -> str:
        return self.__codigo

    @property
    def titulo(self) -> str:
        return self.__titulo

    @property
    def autor(self) -> str:
        return self.__autor
    
    @property
    def precio(self) -> Decimal:
        return self.__precio

    def descripcion(self) -> str:
        return f"Libro: {self.__titulo}, Autor: {self.__autor}, Precio: {self.__precio}"

    def obtener_id(self) -> str:
        return self.__codigo

    def mostrar_detalles(self) -> str:
        return f"Detalles del Libro:\n- Título: {self.__titulo}\n- Autor: {self.__autor}\n- Publicación: {self.__fecha_publicacion}\n- Precio: {self.__precio}"


class Usuario(ElementoBiblioteca):
    def __init__(self, dni: str, nombre: str, fecha_nacimiento: date):
        self.__dni = dni
        self.__nombre = nombre
        self.__fecha_nacimiento = fecha_nacimiento
    
    @property
    def dni(self) -> str:
        return self.__dni
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @property
    def edad(self) -> int:
        hoy = date.today()
        return hoy.year - self.__fecha_nacimiento.year - (
            (hoy.month, hoy.day) < (self.__fecha_nacimiento.month, self.__fecha_nacimiento.day)
        )
    
    def descripcion(self) -> str:
        return f"Usuario: {self.__nombre}, DNI: {self.__dni}, Edad: {self.edad}"

    def obtener_id(self) -> str:
        return self.__dni

    def mostrar_detalles(self) -> str:
        return f"Detalles del Usuario:\n- Nombre: {self.__nombre}\n- DNI: {self.__dni}\n- Fecha de Nacimiento: {self.__fecha_nacimiento}\n- Edad: {self.edad}"


class Prestamo(ElementoBiblioteca):
    def __init__(self, libro: Libro, usuario: Usuario, fecha_prestamo: date, fecha_devolucion: Optional[date] = None):
        self.__libro = libro
        self.__usuario = usuario
        self.__fecha_prestamo = fecha_prestamo
        self.__fecha_devolucion = fecha_devolucion
    
    @property
    def libro(self) -> Libro:
        return self.__libro
    
    @property
    def usuario(self) -> Usuario:
        return self.__usuario
    
    @property
    def fecha_prestamo(self) -> date:
        return self.__fecha_prestamo
    
    @property
    def fecha_devolucion(self) -> Optional[date]:
        return self.__fecha_devolucion
    
    def descripcion(self) -> str:
        if self.__fecha_devolucion:
            return f"Préstamo de '{self.libro.titulo}' a {self.usuario.nombre} devolvido el {self.fecha_devolucion}"
        return f"Préstamo de '{self.libro.titulo}' a {self.usuario.nombre} realizado el {self.fecha_prestamo}"

    def obtener_id(self) -> str:
        return f"Prestamo_{self.libro.codigo}_{self.usuario.dni}"
    
    def mostrar_detalles(self) -> str:
        return f"Detalles del Préstamo:\n- Libro: {self.libro.titulo}\n- Usuario: {self.usuario.nombre}\n- Fecha de Préstamo: {self.fecha_prestamo}\n- Fecha de Devolución: {self.fecha_devolucion if self.fecha_devolucion else 'Pendiente'}"


class Biblioteca:
    def __init__(self):
        self.__elementos: List[ElementoBiblioteca] = []
    
    def agregar_elemento(self, elemento: ElementoBiblioteca) -> None:
        """Agrega un elemento a la biblioteca (puede ser un libro, usuario o préstamo)."""
        self.__elementos.append(elemento)
    
    def listar_elementos(self) -> List[str]:
        """Devuelve una lista con las descripciones de todos los elementos de la biblioteca."""
        return [elemento.descripcion() for elemento in self.__elementos]

    def obtener_elemento_por_id(self, id: str) -> Optional[ElementoBiblioteca]:
        """Obtiene un elemento de la biblioteca por su ID."""
        for elemento in self.__elementos:
            if elemento.obtener_id() == id:
                return elemento
        return None
