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