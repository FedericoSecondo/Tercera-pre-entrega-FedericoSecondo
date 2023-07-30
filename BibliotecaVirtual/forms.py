from django import forms

# ATRAVÉS DE ESTE FORMULARIO SE ESTABLECEN TODAS LAS CLASES QUE SERA POSIBLE INGRESAR A TRAVÉS DE FORMULARIOS "FORMS"

class LibroForm(forms.Form):
    titulo = forms.CharField(label="Titulo del libro", max_length=50, required=True)
    fecha = forms.IntegerField(label="Fecha de Publicacion", required=True)
    editorial = forms.CharField(label="Editorial", max_length=50, required=True)
    generos= (
        (1, "cuento"),
        (2,"novela"),
        (3,"poesia"),
        (4,"enciclopedia"),
    )
    
    genero= forms.ChoiceField(label="Genero", choices= generos, required=True)
    

class InvestigadoresForm (forms.Form):
    nombre = forms.CharField(label="Nombre del Investigador", max_length=50, required=True)
    dni = forms.IntegerField(label="Documento de identiddad", required=True)
    mail = forms.EmailField(label="Email", max_length=50, required=True)
    profesiones= (
        (1, "escritor"),
        (2,"bibliotecologo"),
        (3,"historiador"),
        (4,"profesor"),
        (5,"otro"),
    )
    
    profesion= forms.ChoiceField(label="Profesion", choices= profesiones, required=True)

class UsuariosForm (forms.Form):
    nombre = forms.CharField(label="Nombre del Usuario", max_length=50, required=True)
    dni = forms.IntegerField(label="Documento de identiddad", required=True)
    mail = forms.EmailField(label="Email", max_length=50, required=True)
    direccion= forms.CharField(label="Direccion del Usuario", max_length=50, required=True)
    nacionalidad= (
        (1, "argentino"),
        (2,"uruguayo"),
        (3,"brasileño"),
        (4,"chileno"),
        (5,"otro"),
        )
    
    nacionalidad= forms.ChoiceField(label="Nacionalidad", choices= nacionalidad, required=True) 

class PrestamosForm (forms.Form):
    texto = forms.CharField(label="Texto Prestado", max_length=50, required=True)
    fechaRetiro = forms.DateField(label="Fecha de retirado", required=True)
    fechaDevolucion = forms.DateField(label="Fecha de devolucion", required=True)
    deudor= forms.BooleanField(label="Debe libros anteriores", required=True)
 
    


