# Módulo de Soporte Académico - Registro de Solicitudes

def mostrar_menu():
    """Requerimiento 4: Función sin retorno para mostrar el menú principal."""
    print("\n--- SISTEMA DE SOPORTE ACADÉMICO ---")
    print("1. Registrar nueva solicitud")
    print("2. Ver resumen de solicitudes registradas")
    print("3. Salir")

def validar_texto_obligatorio(prompt):
    """Requerimiento 2 y 6: Función con retorno para validar texto obligatorio (código o nombre)."""
    while True:
        texto = input(prompt).strip()
        if len(texto) >= 3:  # Longitud mínima definida
            return texto
        print("[Error] El texto no puede estar vacío y debe tener al menos 3 caracteres.")

def validar_tipo_consulta():
    """Requerimiento 3: Validar que el tipo pertenezca a la lista básica."""
    tipos_validos = ["matricula", "pagos", "constancia", "plataforma", "otro"]
    while True:
        tipo = input("Ingrese tipo de consulta (matricula, pagos, constancia, plataforma, otro): ").strip().lower()
        if tipo in tipos_validos:
            return tipo
        print(f"[Error] Tipo inválido. Debe elegir entre: {', '.join(tipos_validos)}")

def asignar_prioridad(tipo):
    """Requerimiento 5: Función con retorno para asignar prioridad según el tipo de consulta."""
    if tipo in ["pagos", "matricula"]:
        return "Alta"
    elif tipo in ["constancia", "plataforma"]:
        return "Media"
    else:
        return "Baja"

def mostrar_resumen_solicitud(solicitudes):
    """Requerimiento 7: Función para mostrar el resumen de las solicitudes registradas."""
    print("\n--- RESUMEN DE SOLICITUDES REGISTRADAS ---")
    if not solicitudes:
        print("No hay solicitudes registradas todavía.")
        return
    
    for idx, sol in enumerate(solicitudes, start=1):
        print(f"\nSolicitud #{idx}")
        print(f" - Código Estudiante: {sol['codigo']}")
        print(f" - Nombre: {sol['nombre']}")
        print(f" - Tipo: {sol['tipo']}")
        print(f" - Descripción: {sol['descripcion']}")
        print(f" - Prioridad Asignada: {sol['prioridad']}")

def main():
    # Requerimiento 8 y 9: Control de variables y alcance local en el programa principal
    solicitudes = []
    
    # Requerimiento 10: Permitir registrar al menos tres solicitudes durante una ejecución
    while len(solicitudes) < 3:
        print(f"\n--- Registro de Solicitud ({len(solicitudes) + 1}/3) ---")
        mostrar_menu()
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            codigo = validar_texto_obligatorio("Ingrese código de estudiante: ")
            nombre = validar_texto_obligatorio("Ingrese nombre del estudiante: ")
            tipo = validar_tipo_consulta()
            descripcion = input("Ingrese descripción breve del caso: ").strip()
            
            prioridad = asignar_prioridad(tipo)
            
            solicitud = {
                "codigo": codigo,
                "nombre": nombre,
                "tipo": tipo,
                "descripcion": descripcion,
                "prioridad": prioridad
            }
            solicitudes.append(solicitud)
            print(f"¡Solicitud registrada con éxito! Prioridad asignada: {prioridad}")
            
        elif opcion == "2":
            mostrar_resumen_solicitud(solicitudes)
            
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("[Error] Opción no válida. Intente de nuevo.")
            
    if len(solicitudes) == 3:
        print("\n¡Se alcanzó el límite de 3 solicitudes requeridas por sesión!")
        mostrar_resumen_solicitud(solicitudes)

if __name__ == "__main__":
    main()