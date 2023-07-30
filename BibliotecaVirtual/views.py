from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import LibroForm
from .forms import InvestigadoresForm
from .forms import UsuariosForm
from .forms import PrestamosForm



# Create your views here.
def index(request):
    return render(request,"BibliotecaVirtual/base.html")

def libros(request):
    ctx = {"libros": Libro.objects.all() }
    return render(request, "BibliotecaVirtual/libros.html", ctx)
def investigadores(request):
    ctx = {"investigadores": Investigadores.objects.all() }
    return render(request, "BibliotecaVirtual/investigadores.html", ctx)
def usuarios(request):
    ctx = {"usuarios": Usuarios.objects.all() }
    return render(request, "BibliotecaVirtual/usuarios.html", ctx)
def prestamos(request):
    ctx = {"prestamos": Prestamos.objects.all() }
    return render(request, "BibliotecaVirtual/prestamos.html", ctx)

def libroForm(request):
    if request.method == "POST":
        libro=Libro(titulo=request.POST["titulo"],fecha=request.POST["fecha"],editorial=request.POST["editorial"])
        libro.save()
        return HttpResponse ("Se ha ingresado con exito el libro!")
    return render (request, "BibliotecaVirtual/libroForm.html")



def libroForm2 (request): #ESTA FUNCION PERMITE CARGAR UN LIBRO A TRAVÉS DE UN FORMULARIO
    if request.method == "POST":
        miForm=LibroForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion=miForm.cleaned_data
            libro=Libro(titulo=informacion["titulo"], fecha=informacion["fecha"], editorial=informacion["editorial"])
            libro.save()
            return render (request, "BibliotecaVirtual/base.html")
    else:
        miForm=LibroForm()

        miForm = LibroForm()
    return render(request, "BibliotecaVirtual/libroForm2.html", {"form": miForm})

def buscarTitulo(request):
    return render(request, "BibliotecaVirtual/buscarTitulo.html")

def buscar2(request): # ESTA FUNCION PERMITE BUSCAR UN LIBRO POR SU TITULO 
    if request.method == 'GET':
        titulo = request.GET['titulo']
        if titulo: 
            libros = Libro.objects.filter(titulo__icontains=titulo)
            return render(request, 
                        "BibliotecaVirtual/resultadosTitulo.html", 
                        {"titulo": titulo, "libros":libros})
        else:
            return HttpResponse("No se ingresaron datos para buscar!")

    return HttpResponse("No se ingresaron datos para buscar!")

    

def investigadoresForm (request): #ESTA FUNCION PERMITE CARGAR INVESTIGADORES A TRAVÉS DE UN FORMULARIO
    if request.method == "POST":
        miForm=InvestigadoresForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion=miForm.cleaned_data
            investigador=Investigadores(nombre=informacion["nombre"], dni=informacion["dni"], mail=informacion["mail"])
            investigador.save()
            return render (request, "BibliotecaVirtual/base.html")
    else:
        miForm=InvestigadoresForm()

        miForm = InvestigadoresForm()
    return render(request, "BibliotecaVirtual/investigadoresForm.html", {"form": miForm})  

def usuariosForm (request): # ESTA FUNCION PERMITE CARGAR UN USUARIO A TRAVÉS DE UN FORMULARIO
    if request.method == "POST":
        miForm=UsuariosForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion=miForm.cleaned_data
            usuario=Usuarios(nombre=informacion["nombre"], dni=informacion["dni"], mail=informacion["mail"], direccion=informacion["direccion"])
            usuario.save()
            return render (request, "BibliotecaVirtual/base.html")
    else:
        miForm=UsuariosForm()

        miForm = UsuariosForm()
    return render(request, "BibliotecaVirtual/usuariosForm.html", {"form": miForm})  

def prestamosForm (request): # ESTA FUNCION PERMITE ESTABLECER LOS LIBROS QUE ESTA EN PRESTAMO Y SI QUIEN LO TOMO PRESTADO DEBE ALGUN LIBRO
    if request.method == "POST":
        miForm=PrestamosForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion=miForm.cleaned_data
            prestamo=Prestamos(texto=informacion["texto"], fechaRetiro=informacion["fechaRetiro"], fechaDevolucion=informacion["fechaDevolucion"], deudor=informacion["deudor"])
            prestamo.save()
            return render (request, "BibliotecaVirtual/base.html")
    else:
        miForm=PrestamosForm()

        miForm = PrestamosForm()
    return render(request, "BibliotecaVirtual/prestamosForm.html", {"form": miForm}) 
                    




