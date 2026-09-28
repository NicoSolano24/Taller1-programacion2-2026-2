# ===================================================================
# utilidades.py - Funciones de validacion y entrada de datos
# ===================================================================
# Estudiante: Nicolas David Solano Plazas
# Código: 106202524246
# ===================================================================

from cliente import Cliente


def leer_opcion_valida(mensaje, opciones):
    while True:
        entrada = input(mensaje).strip().lower()
        if entrada in opciones:
            return entrada
        print(f"  Opcion no valida. Las opciones son: {', '.join(opciones)}")


def leer_numero_positivo(mensaje):
    while True:
        entrada = input(mensaje).strip()
        if entrada.isdigit() and int(entrada) > 0:
            return int(entrada)
        print("  Debe ingresar un numero entero mayor que 0.")


def leer_telefono(mensaje):
    """
    Pide al usuario que ingrese un numero de telefono.
    Valida que tenga exactamente 10 digitos y solo contenga numeros.
    """
    while True:
        entrada = input(mensaje).strip()
        if entrada.isdigit() and len(entrada) == 10:
            return entrada
        print("  El telefono debe tener exactamente 10 digitos y solo contener numeros.")


def registrar_cliente_por_consola(consultorio):
    print("\n" + "-" * 50)
    print("  REGISTRO DE NUEVO PACIENTE")
    print("-" * 50)

    # Validar que el documento (cedula o TI) no este repetido ni vacio, y que sean solo numeros
    while True:
        cedula = input("  Documento (Cedula o Tarjeta de Identidad): ").strip()
        if cedula == "":
            print("  El documento no puede estar vacio.")
        elif not cedula.isdigit():
            print("  El documento debe contener solo numeros.")
        elif consultorio.existe_cedula(cedula):
            print(f"  Ya existe un paciente con el documento {cedula}. Ingrese otro.")
        else:
            break

    while True:
        nombre = input("  Nombre completo: ").strip()
        if nombre != "":
            break
        print("  El nombre no puede estar vacio.")

    # Usar la nueva funcion para validar telefonos colombianos (10 digitos)
    telefono = leer_telefono("  Telefono (10 digitos): ")

    tipo_cliente = leer_opcion_valida(
        "  Tipo de paciente (particular / eps / prepagada): ",
        ["particular", "eps", "prepagada"]
    )

    tipo_atencion = leer_opcion_valida(
        "  Tipo de atencion (limpieza / calzas / extraccion / diagnostico): ",
        ["limpieza", "calzas", "extraccion", "diagnostico"]
    )

    if tipo_atencion in ["calzas", "extraccion"]:
        cantidad = leer_numero_positivo("  Cantidad (numero de piezas): ")
    else:
        cantidad = 1
        print(f"  Cantidad: 1 (fija para {tipo_atencion})")

    prioridad = leer_opcion_valida(
        "  Prioridad de atencion (normal / urgente): ",
        ["normal", "urgente"]
    )

    fecha = input("  Fecha de la cita (DD-MM-AAAA): ").strip()

    nuevo_cliente = Cliente(
        cedula, nombre, telefono,
        tipo_cliente, tipo_atencion, cantidad,
        prioridad, fecha
    )

    consultorio.registrar_cliente(nuevo_cliente)

    print(f"\n  Paciente '{nombre}' registrado con exito.")
    print(f"  Valor total del servicio: ${nuevo_cliente.valor_total:,.0f}\n")


def cargar_datos_de_prueba(consultorio):
    datos_prueba = [
        ("1053876234", "Ana Maria Perez", "3101234567",
         "Particular", "Extraccion", 2, "Urgente", "27-09-2026"),

        ("1098234567", "Luis Fernando Gomez", "3204567890",
         "EPS", "Limpieza", 1, "Normal", "27-09-2026"),

        ("1075345678", "Marta Lucia Diaz", "3007891234",
         "Prepagada", "Calzas", 3, "Normal", "28-09-2026"),

        ("1090456789", "Juan Pablo Ruiz", "3113214567",
         "Particular", "Diagnostico", 1, "Normal", "29-09-2026"),

        ("1087567890", "Sofia Valentina Cely", "3156547890",
         "EPS", "Extraccion", 1, "Urgente", "30-09-2026"),

        ("1064789012", "Carlos Andres Mendoza", "3189012345",
         "Particular", "Limpieza", 1, "Normal", "01-10-2026"),

        ("1023456789", "Maria Fernanda Torres", "3012345678",
         "EPS", "Calzas", 2, "Normal", "02-10-2026"),

        ("1045678901", "Diego Alejandro Vargas", "3145678901",
         "Prepagada", "Extraccion", 2, "Urgente", "03-10-2026"),

        ("1078901234", "Valentina Castro Lopez", "3178901234",
         "Particular", "Calzas", 4, "Urgente", "04-10-2026"),

        ("1034567890", "Andres Felipe Rivera", "3034567890",
         "Prepagada", "Diagnostico", 1, "Normal", "05-10-2026"),
    ]

    for datos in datos_prueba:
        consultorio.registrar_cliente(Cliente(*datos))

    print(f"  Se cargaron {len(datos_prueba)} pacientes de prueba para demostracion.")
