# Tercera-pre-entrega-FedericoSecondo
Biblioteca vitual: Se trata de una biblioteca que contiene libros de Jorge Luid Borges
Libros: Cada libro (creado a través de la clase Libro) contiene titulo, fecha de publicación y editorial
Los libros se pueden cargar a través de un formulario FORMS a través de la url libro_form2/
Usuarios: La pagina contiene la  Usuarios (creados a través de la clase Usuarios) contiene nombre , dni, mail y dirección
Los usuarios se pueden cargar a través de un formulario FORMS a través de la url usuarios_form/
Invesigadores: Cada investigador(creado a través de la clase Investigadores) contiene nombre, dni, mail
Los investigadores se pueden cargar a través de un formulario FORMS a traés de la url investigadores_form/
Prestamos: Se pueden establecer los libros que han sido prestados y si la persona que lo tomo es deudor de otro libro
Los prestamos se pueden cargar a través de un formulario FORMS  a través de la url prestamos_form/
Boton de Inicio: permite al navegador ir a la pagina de inicio donde se muestra una cabecera, fotos de autores (Borges, Bioy Casares, Sabato), y un pie de pagina
Las vistas de : Libro, Investigadores, Usuario y Prestamos heredan el template HTML principal, por lo que todas las vistas contienen la misma cabecera y el mismo pie
Boton Administración: permite gestionar la base de datos y agregar, borrar : Libros,Usuarios,Investigadores,Prestamos.
Función Buscar: establecida a través de la funcion buscar2 (en views) nos pemite buscar un libro a través del metodo GET en la base de datos creada.
