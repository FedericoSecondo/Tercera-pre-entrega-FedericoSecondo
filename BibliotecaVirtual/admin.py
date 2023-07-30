from django.contrib import admin
from .models import Libro, Investigadores, Usuarios, Prestamos
# Register your models here.


# Register your models here.
admin.site.register(Libro)
admin.site.register(Investigadores)
admin.site.register(Usuarios)
admin.site.register(Prestamos)