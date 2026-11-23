# Sistema Integral de Gestion - Software FJ

## Descripcion del proyecto

Este proyecto consiste en el desarrollo de un sistema de gestion para la empresa Software FJ, como parte de la actividad academica del curso de Programacion de la Universidad Nacional Abierta y a Distancia (UNAD).

El sistema permite administrar clientes, servicios y reservaciones mediante programacion orientada a objetos. Funciona desde una aplicacion de consola y utiliza listas internas para almacenar la informacion durante su ejecucion, sin necesidad de una base de datos.

## Objetivo

Desarrollar una aplicacion que permita gestionar clientes, servicios y reservaciones de Software FJ, aplicando conceptos de programacion orientada a objetos, validacion de datos, manejo de excepciones y registro de eventos.

## Funcionalidades principales

- Registro y validacion de clientes.
- Registro de servicios.
- Reservas de salas.
- Alquiler de equipos.
- Asesorias especializadas.
- Creacion, confirmacion y cancelacion de reservaciones.
- Procesamiento de reservaciones confirmadas.
- Calculo de costos con descuentos e impuestos opcionales.
- Consulta de clientes, servicios y reservaciones.
- Manejo de errores mediante excepciones personalizadas.
- Registro de eventos y errores en un archivo de log.

## Archivos del proyecto

- entidades.py: contiene la clase abstracta Entidad.
- clientes.py: contiene la clase Cliente y sus validaciones.
- servicios.py: contiene la clase abstracta Servicio y los tres servicios especializados.
- reservas.py: gestiona las reservaciones, sus estados y el calculo de costos.
- excepciones.py: contiene las excepciones personalizadas.
- registro.py: configura el registro de eventos y errores.
- gestion.py: administra clientes, servicios y reservaciones.
- pruebas.py: contiene las pruebas de funcionamiento.
- main.py: contiene el menu principal de la aplicacion.

## Conceptos de programacion orientada a objetos

El proyecto aplica los siguientes conceptos:

- Abstraccion: mediante las clases abstractas Entidad y Servicio.
- Herencia: las clases Cliente y los servicios especializados heredan de sus respectivas clases base.
- Encapsulamiento: se utilizan atributos privados y propiedades para controlar el acceso a los datos.
- Polimorfismo: los diferentes servicios implementan sus propios metodos para describir y calcular sus costos.
- Parametros opcionales: el calculo de costos permite aplicar descuentos e impuestos.

## Manejo de excepciones y registro de eventos

El sistema utiliza excepciones personalizadas para controlar errores de validacion y operaciones no permitidas.

Tambien implementa las estructuras try, except, else y finally, junto con el encadenamiento de excepciones.

Los eventos, advertencias y errores se registran en el archivo software_fj.log, que se genera durante la ejecucion del programa.

## Ejecucion del proyecto

Para iniciar la aplicacion, abre una terminal en la carpeta del proyecto y ejecuta:

    python main.py

Para ejecutar las pruebas de funcionamiento:

    python pruebas.py

## Pruebas realizadas

Se desarrollaron 23 pruebas para verificar diferentes escenarios del sistema:

- Registro correcto e incorrecto de clientes.
- Creacion valida e invalida de servicios.
- Creacion de reservaciones.
- Intentos de reservar servicios no disponibles.
- Confirmacion y cancelacion de reservaciones.
- Procesamiento de reservaciones.
- Validacion de estados.
- Calculo de costos con descuentos e impuestos.
- Comportamiento polimorfico de los servicios.
