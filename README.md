# Soporte Académico

Sistema de soporte académico desarrollado en Python para registrar y gestionar solicitudes de estudiantes.

## Objetivo

El sistema permite registrar solicitudes de soporte académico, validar los datos ingresados, asignar una prioridad según el tipo de consulta y mostrar las solicitudes registradas.

## Funcionalidades

- Registrar solicitudes de estudiantes.
- Validar el código del estudiante.
- Validar el nombre del estudiante.
- Validar la descripción de la solicitud.
- Validar el tipo de consulta.
- Asignar prioridad automáticamente.
- Mostrar las solicitudes registradas.
- Contabilizar las solicitudes registradas.
- Permitir salir correctamente del sistema.

## Tipos de consulta

El sistema permite registrar los siguientes tipos de consulta:

- `matricula`
- `pagos`
- `constancia`
- `plataforma`
- `otro`

## Validaciones

El sistema realiza las siguientes validaciones:

### Código del estudiante

El código debe tener como mínimo 5 caracteres.

Ejemplo de error:

```text
ERROR: El código debe tener al menos 5 caracteres.
## Análisis del problema

El sistema de soporte académico tiene como finalidad organizar y gestionar las solicitudes realizadas por los estudiantes. El problema identificado es la necesidad de contar con un mecanismo que permita registrar correctamente los datos de cada solicitud y validar la información ingresada.

Cuando los datos no son validados, pueden registrarse códigos incompletos, nombres vacíos, descripciones sin contenido o tipos de consulta que no corresponden a las opciones establecidas. Además, es necesario identificar la prioridad de cada solicitud para facilitar su atención.

Por este motivo, se desarrolló un sistema en Python que permite registrar solicitudes, validar los datos ingresados, asignar automáticamente una prioridad y mostrar las solicitudes almacenadas.

## Requisitos del sistema

### Requisitos funcionales

- RF01: El sistema debe permitir registrar una solicitud de soporte académico.
- RF02: El sistema debe solicitar el código del estudiante.
- RF03: El sistema debe solicitar el nombre del estudiante.
- RF04: El sistema debe solicitar el tipo de consulta.
- RF05: El sistema debe solicitar una descripción de la solicitud.
- RF06: El sistema debe validar que el código tenga como mínimo 5 caracteres.
- RF07: El sistema debe validar que el nombre no esté vacío.
- RF08: El sistema debe validar que la descripción no esté vacía.
- RF09: El sistema debe validar que el tipo de consulta sea válido.
- RF10: El sistema debe asignar automáticamente una prioridad.
- RF11: El sistema debe permitir mostrar las solicitudes registradas.
- RF12: El sistema debe mostrar el total de solicitudes registradas.
- RF13: El sistema debe permitir finalizar correctamente el programa.

### Requisitos no funcionales

- RNF01: El sistema debe desarrollarse utilizando Python.
- RNF02: El sistema debe ejecutarse desde una terminal.
- RNF03: El sistema debe presentar mensajes claros para el usuario.
- RNF04: El sistema debe utilizar funciones para organizar el código.
- RNF05: El sistema debe validar los datos antes de registrar una solicitud.
- RNF06: El código debe mantenerse organizado y documentado.
## Tabla de requisitos y funciones

| Requisito | Función relacionada | Descripción |
|---|---|---|
| RF01 | `ingresar_solicitud()` | Permite registrar una solicitud. |
| RF02 | `validar_codigo()` | Valida el código del estudiante. |
| RF03 | `validar_texto()` | Valida que el nombre no esté vacío. |
| RF04 | `validar_tipo_consulta()` | Valida el tipo de consulta. |
| RF05 | `validar_texto()` | Valida que la descripción no esté vacía. |
| RF06 | `validar_codigo()` | Comprueba que el código tenga al menos 5 caracteres. |
| RF07 | `validar_texto()` | Comprueba que el nombre tenga contenido. |
| RF08 | `validar_texto()` | Comprueba que la descripción tenga contenido. |
| RF09 | `validar_tipo_consulta()` | Comprueba que el tipo sea válido. |
| RF10 | `calcular_prioridad()` | Asigna la prioridad automáticamente. |
| RF11 | `mostrar_solicitudes()` | Muestra las solicitudes registradas. |
| RF12 | `len(solicitudes)` | Permite contabilizar las solicitudes. |
| RF13 | `break` | Finaliza el programa correctamente. |
## Tabla de requisitos y pruebas

| Requisito | Prueba realizada | Resultado |
|---|---|---|
| RF01 | Registrar una solicitud con datos válidos | Correcto |
| RF06 | Ingresar un código con menos de 5 caracteres | Error controlado |
| RF07 | Ingresar un nombre vacío | Error controlado |
| RF08 | Ingresar una descripción vacía | Error controlado |
| RF09 | Ingresar un tipo de consulta no permitido | Error controlado |
| RF10 | Registrar una consulta de plataforma | Prioridad Alta |
| RF10 | Registrar una consulta de pagos | Prioridad Media |
| RF10 | Registrar una consulta de constancia u otro | Prioridad Baja |
| RF11 | Seleccionar la opción 2 | Solicitudes mostradas |
| RF12 | Registrar varias solicitudes | Total contabilizado |
| RF13 | Seleccionar la opción 3 | Programa finalizado correctamente |
## Pseudocódigo del sistema

INICIO

Mostrar menú principal.

Mientras el usuario no seleccione "Salir":

    Mostrar opciones:
        1. Registrar solicitud
        2. Mostrar solicitudes
        3. Salir

    Leer opción.

    Si opción = 1:
        Solicitar código del estudiante.
        Validar código.
        Solicitar nombre.
        Validar nombre.
        Solicitar tipo de consulta.
        Validar tipo de consulta.
        Solicitar descripción.
        Validar descripción.
        Calcular prioridad.
        Registrar solicitud.
        Mostrar confirmación.

    Si opción = 2:
        Mostrar las solicitudes registradas.
        Mostrar el total de solicitudes.

    Si opción = 3:
        Mostrar mensaje de finalización.
        Terminar programa.

    Si la opción no es válida:
        Mostrar mensaje de error.

FIN
## Reflexión sobre el trabajo realizado

El desarrollo del sistema de Soporte Académico permitió aplicar los conocimientos adquiridos en programación con Python. Durante el desarrollo se utilizaron funciones, estructuras condicionales, listas, diccionarios y validaciones para organizar el funcionamiento del programa.

Una parte importante fue implementar validaciones para evitar el ingreso de datos incorrectos. También se utilizó una función para calcular automáticamente la prioridad de cada solicitud según el tipo de consulta.

El uso de Git y GitHub permitió mantener un registro de los cambios realizados durante el desarrollo. Esto facilita organizar el proyecto y realizar modificaciones de manera controlada.

Finalmente, las pruebas realizadas permitieron comprobar el funcionamiento del sistema utilizando datos válidos e inválidos, identificando errores y verificando que el programa responda correctamente ante diferentes situaciones.
## Conclusiones

1. El sistema permite registrar y organizar solicitudes de soporte académico mediante una estructura sencilla y ordenada.

2. Las funciones de validación ayudan a evitar el registro de información incorrecta, como códigos demasiado cortos, nombres vacíos, descripciones vacías o tipos de consulta no permitidos.

3. La asignación automática de prioridades permite diferenciar las solicitudes según el tipo de consulta registrada.

4. Las pruebas realizadas permitieron comprobar el comportamiento del sistema con diferentes datos y situaciones.

5. El uso de Git y GitHub permitió registrar los avances del proyecto y mantener un historial de los cambios realizados.

6. El desarrollo del proyecto permitió reforzar los conocimientos de programación en Python y mejorar la organización del código mediante funciones.
## Declaración de uso de inteligencia artificial

Durante el desarrollo del proyecto se utilizó inteligencia artificial como herramienta de apoyo para comprender conceptos de programación, revisar la estructura del código, identificar posibles errores y mejorar la documentación del proyecto.

La implementación, ejecución y comprobación del funcionamiento del sistema fueron realizadas por el estudiante. Las respuestas obtenidas mediante inteligencia artificial fueron revisadas y adaptadas de acuerdo con las necesidades del proyecto.

La inteligencia artificial fue utilizada como apoyo al aprendizaje y no como sustituto de la comprensión y participación del estudiante en el desarrollo del trabajo.
## Evidencias de funcionamiento

Durante las pruebas del sistema se verificaron diferentes situaciones:

- Registro de solicitudes con datos válidos.
- Validación de códigos con menos de 5 caracteres.
- Validación de nombres vacíos.
- Validación de descripciones vacías.
- Validación de tipos de consulta no permitidos.
- Asignación de prioridad Alta para consultas de plataforma.
- Asignación de prioridad Media para consultas de pagos.
- Asignación de prioridad Baja para consultas como constancia.
- Registro de tres o más solicitudes.
- Visualización de las solicitudes registradas.
- Conteo total de solicitudes.
- Finalización correcta del programa.

Las capturas de pantalla de estas pruebas se utilizan como evidencia del funcionamiento del sistema y permiten comprobar que las validaciones y funcionalidades implementadas responden de acuerdo con lo esperado.
## Estado final del proyecto

El proyecto Soporte Académico se encuentra implementado y documentado. El sistema permite registrar solicitudes, validar los datos ingresados, calcular automáticamente la prioridad y mostrar las solicitudes almacenadas.

Se realizaron pruebas con datos válidos e inválidos para comprobar las principales funcionalidades del programa.

El proyecto se encuentra almacenado en GitHub y cuenta con un historial de cambios mediante commits.

### Tecnologías utilizadas

- Python
- Visual Studio Code
- Git
- GitHub

### Autor

Frank Andersson