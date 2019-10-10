#Physic-storm

## Notas:

### Creo la base de datos.

`python manage.py migrate`

### Correr server:

`python manage.py runserver <- Corre en puerto 8000`

### Agregar apps:

`py manage.py startapp <nombre_app>`

### instalar bootstrap en caso de que no lo haya instalado en el env

`pip install django-bootstrap4`

###Actualizar los cambios en los modelos de datos

`pyhton3 manage.py makemigrations`
`python3 manage.py migrate`

### Integrantes:

Gonzalo Durán Sáez 201473507-3
Jorge Galleguillos 201473545-6

### Nombre proyecto:

Physic-Storm

Nos adelantamos a nuestra era, y instalamos bootstrap para crear un navbar, asi que en caso de no compilar, por favor ejecutar: pip install django-bootstrap4

### Usuario para test:

Casi todos los sitios del sitio son accesibles solo por usuarios, por lo que se permite usar el siguiente usuario para probar el sitio:
username: tester
password: holachao

El formulario con las request pedidas para la Entrega 5 están todas en la sección "Material -> Contenidos"

# Entrega 6

`forms.py` se utilizo para el formulario de creacion de cuentas, en el caso de las materias y preguntas aun no se implementa 
un metodo para añadir objetos a la base de datos debido a que no es necesario para el funcionamiento del proyecto.

## Como funciona el proyecto?

Antes que todo, es necesario tener una cuenta registrada en la base de datos para poder acceder al sitio. 
Si es que no se tiene una, se puede utilizar un formulario para crearla.

Dentro del sitio, la mayoria de la funcionalidad se encuentra en el dropdown _contenidos_, el cual contiene dos opciones:

* __Material de Estudio__:  En este sitio, se le pedira elegir los topicos que desee ver (en nuestro caso, topicos pueder ser visto como los contenidos que encapsula cada certamen)
, posteriormente se debera elegir los subtopicos del material a solicitar, se le presentara opciones de material de estudio. Estos son capitulos relevantes del libro de la materia en
formato _pdf_.

* __Generador de Certamenes__: En este sitio, se eligira una de los tres topicos disponibles (junto a la opcion de generar un certamen con todas los topicos disponibles), 
el sistema eligira tres preguntas aleatorias del pool que contenga y se las presentara al usuario en una misma pagina. Para poder ver la solucion de tales preguntas, se debera
presionar el boton _Ver Solucion_.

* __Datos Necesarios__: Para poder correr de forma correcta el proyecto, es necesario tener ejercicios en la carpeta `templates` (codigo `HTML` de estos), junto a sus imagenes en la carpeta `static`.
En esta entrega se incluyen ejercicios, por ahora no se incluye forma de parsearlos desde su formato original `.tex` a un `HTML` compatible con este sitio, debido a la complejidad de la generacion de estos.

Para poder visualizar las ecuaciones en el sitio, es necesario permitir la ejecucion del script [MathJax](https://www.mathjax.org/).