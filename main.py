def mostrar_menu():
    print("\n======================================")
    print("       SOPORTE ACADÉMICO")
    print("======================================")
    print("1. Registrar solicitud")
    print("2. Mostrar solicitudes")
    print("3. Salir")
    print("======================================")


# ------------------------------------------------------------
# FUNCIÓN CON RETORNO: validar texto obligatorio
# ------------------------------------------------------------
def validar_texto(texto):
    return texto.strip() != ""


# ------------------------------------------------------------
# FUNCIÓN CON RETORNO: validar código del estudiante
# ------------------------------------------------------------
def validar_codigo(codigo):
    return codigo.strip() != "" and len(codigo.strip()) >= 5


# ------------------------------------------------------------
# FUNCIÓN CON RETORNO: validar tipo de consulta
# ------------------------------------------------------------
def validar_tipo_consulta(tipo):
    tipos_validos = [
        "matricula",
        "pagos",
        "constancia",
        "plataforma",
        "otro"
    ]

    return tipo.lower().strip() in tipos_validos


# ------------------------------------------------------------
# FUNCIÓN CON RETORNO: calcular prioridad
# ------------------------------------------------------------
def calcular_prioridad(tipo):
    tipo = tipo.lower().strip()

    if tipo == "plataforma":
        return "Alta"
    elif tipo == "pagos":
        return "Media"
    else:
        return "Baja"


# ------------------------------------------------------------
# FUNCIÓN CON RETORNO: registrar solicitud
# ------------------------------------------------------------
def registrar_solicitud(codigo, nombre, tipo, descripcion):

    prioridad = calcular_prioridad(tipo)

    solicitud = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo": tipo,
        "descripcion": descripcion,
        "prioridad": prioridad
    }

    return solicitud


# ------------------------------------------------------------
# FUNCIÓN SIN RETORNO: mostrar resumen
# ------------------------------------------------------------
def mostrar_resumen(solicitud):

    print("\n======================================")
    print("       RESUMEN DE SOLICITUD")
    print("======================================")
    print(f"Código: {solicitud['codigo']}")
    print(f"Nombre: {solicitud['nombre']}")
    print(f"Tipo de consulta: {solicitud['tipo']}")
    print(f"Descripción: {solicitud['descripcion']}")
    print(f"Prioridad: {solicitud['prioridad']}")
    print("======================================")


# ------------------------------------------------------------
# FUNCIÓN: registrar una solicitud con validaciones
# ------------------------------------------------------------
def ingresar_solicitud():

    print("\n===== REGISTRO DE SOLICITUD =====")

    codigo = input("Ingrese código del estudiante: ")
    nombre = input("Ingrese nombre del estudiante: ")
    tipo = input("Ingrese tipo de consulta: ")
    descripcion = input("Ingrese una descripción: ")

    # Validar código
    if not validar_codigo(codigo):
        print("\nERROR: El código debe tener al menos 5 caracteres.")
        return None

    # Validar nombre
    if not validar_texto(nombre):
        print("\nERROR: El nombre no puede estar vacío.")
        return None

    # Validar tipo de consulta
    if not validar_tipo_consulta(tipo):
        print("\nERROR: Tipo de consulta no válido.")
        print("Tipos permitidos:")
        print("- matricula")
        print("- pagos")
        print("- constancia")
        print("- plataforma")
        print("- otro")
        return None

    # Validar descripción
    if not validar_texto(descripcion):
        print("\nERROR: La descripción no puede estar vacía.")
        return None

    # Registrar solicitud
    solicitud = registrar_solicitud(
        codigo,
        nombre,
        tipo,
        descripcion
    )

    print("\nSolicitud registrada correctamente.")

    return solicitud


# ------------------------------------------------------------
# FUNCIÓN: mostrar todas las solicitudes
# ------------------------------------------------------------
def mostrar_solicitudes(solicitudes):

    print("\n======================================")
    print("      SOLICITUDES REGISTRADAS")
    print("======================================")

    if len(solicitudes) == 0:
        print("No hay solicitudes registradas.")
        return

    for i, solicitud in enumerate(solicitudes, start=1):

        print(f"\n--- Solicitud {i} ---")
        print(f"Código: {solicitud['codigo']}")
        print(f"Nombre: {solicitud['nombre']}")
        print(f"Tipo: {solicitud['tipo']}")
        print(f"Descripción: {solicitud['descripcion']}")
        print(f"Prioridad: {solicitud['prioridad']}")

    print("\n======================================")


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

solicitudes = []

print("\n****************************************")
print("* SISTEMA DE SOPORTE ACADÉMICO        *")
print("* Registro de solicitudes              *")
print("****************************************")

while True:

    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    # --------------------------------------------------------
    # OPCIÓN 1: REGISTRAR SOLICITUD
    # --------------------------------------------------------
    if opcion == "1":

        solicitud = ingresar_solicitud()

        if solicitud is not None:

            solicitudes.append(solicitud)

            print(f"\nTotal de solicitudes registradas: {len(solicitudes)}")

            if len(solicitudes) >= 3:
                print("Ya se registraron al menos 3 solicitudes.")

    # --------------------------------------------------------
    # OPCIÓN 2: MOSTRAR SOLICITUDES
    # --------------------------------------------------------
    elif opcion == "2":

        mostrar_solicitudes(solicitudes)

    # --------------------------------------------------------
    # OPCIÓN 3: SALIR
    # --------------------------------------------------------
    elif opcion == "3":

        print("\n======================================")
        print("Gracias por utilizar el sistema.")
        print(f"Total de solicitudes: {len(solicitudes)}")
        print("Programa finalizado correctamente.")
        print("======================================")

        break

    # --------------------------------------------------------
    # OPCIÓN INCORRECTA
    # --------------------------------------------------------
    else:

        print("\nERROR: Opción no válida.")
        print("Seleccione 1, 2 o 3.")