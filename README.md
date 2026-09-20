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
- Contabilizar las solicitudes.
- Finalizar correctamente el programa.

## Tipos de consulta

- Matrícula
- Pagos
- Constancia
- Plataforma
- Otro

## Prioridades

| Tipo de consulta | Prioridad |
|---|---|
| Plataforma | Alta |
| Pagos | Media |
| Matrícula | Baja |
| Constancia | Baja |
| Otro | Baja |

## Tecnologías utilizadas

- Python
- Visual Studio Code
- Git
- GitHub

## Validaciones

El sistema verifica que:

- El código del estudiante tenga al menos 5 caracteres.
- El nombre no esté vacío.
- La descripción no esté vacía.
- El tipo de consulta pertenezca a los tipos permitidos.

## Pruebas realizadas

Se realizaron pruebas de:

1. Registro de solicitudes.
2. Consulta de solicitudes registradas.
3. Validación de código incorrecto.
4. Validación de tipo de consulta incorrecto.
5. Asignación de prioridad alta.
6. Asignación de prioridad media.
7. Asignación de prioridad baja.
8. Salida correcta del sistema.

## Ejemplo de funcionamiento

```text
SOPORTE ACADÉMICO

1. Registrar solicitud
2. Mostrar solicitudes
3. Salir