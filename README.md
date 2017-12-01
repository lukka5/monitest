# MONI test

Se debe desarrollar sitio web en el que se registran pedido de prestamos
de usuarios que acceden a el.  El usuario no necesita registrarse para
solicitar un préstamo.  Para definir si al usuario se le aprueba o no el
préstamoo usaremos una API definida debajo.

endpoint: http://scoringservice.moni.com.ar:7001/api/v1/scoring/
ejemplo:
http://scoringservice.moni.com.ar:7001/api/v1/scoring/?document_number=30156149&gender=M&email=fran@mail.com
ACLARACION: usar esta api, no implementarla.

El formulario de pedido de prestamos el usuario debe ingresar dni,
nombre y apellido, genero, email y monto solicitado.  El usuario luego
de ingresar los datos debe recibir la respuesta negativa o positiva en
la misma página que ingreso sus datos.  Contemplar casos de datos
ingresados con errores.

También se debe desarrollarse un sitio de administración en el que se
puedan ver los pedidos de préstamo, con la opción de editarlos y
eliminarlos. A este sitio solo pueden acceder usuarios administradores.
No usar admin de Django.

## Installation

    pip install -r requirements.txt
    python manage.py createsuperuser
    python manage.py migrate
    python manage.py runserver

## Urls

    # Publico
    /loans/petition/  # Nuevo pedido de prestamo

    # Solo admin
    /loans/             # Ver todos los pedidos de prestamo (y borrar)
    /loans/<id>/        # Actualizar un pedido de prestamo en particular
