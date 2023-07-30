from django.db import models

# Create your models here.
class Libro(models.Model): # CLASE DONDE SE ESTABLECEN LOS DATOS PARA CREAR LIBROS
    titulo=models.CharField(max_length=50)
    fecha=models.IntegerField()
    editorial=models.CharField(max_length=50)
        
    def __str__(self) -> str:
        return f"{self.titulo}"

class Investigadores(models.Model): # CLASE DONDE SE ESTABLECEN LOS DATOS PARA CREAR INVESTIGADORES
    nombre=models.CharField(max_length=50)
    dni=models.IntegerField()
    mail=models.EmailField()

    def __str__(self) -> str:
        return f"{self.nombre}"

class Usuarios  (models.Model): # CLASE DONDE SE ESTABLECEN LOS DATOS PARA CREAR USUARIOS
    nombre=models.CharField(max_length=50)
    dni=models.IntegerField()
    mail=models.EmailField()
    direccion=models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.nombre}"

class Prestamos(models.Model): # CLASE DONDE SE ESTABLECEN LOS DATOS PARA CREAR LIBROS QUE SE DAN EN PRESTAMO
    texto=models.CharField(max_length=50)
    fechaRetiro=models.DateField()
    fechaDevolucion=models.DateField()
    deudor=models.BooleanField()

    def __str__(self) -> str:
        return f"{self.texto} {self.fechaDevolucion}"