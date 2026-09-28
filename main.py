# ===================================================================
# main.py - Punto de entrada del programa
# ===================================================================
# Taller 1 - Consultorio Odontologico
# Programacion 2 - Universidad de Manizales (2026-2)
# Estudiante: Nicolas David Solano Plazas
# Código: 106202524246
# ===================================================================

from consultorio import Consultorio
from utilidades import (
    registrar_cliente_por_consola,
    cargar_datos_de_prueba,
    leer_opcion_valida
)


def mostrar_menu():
    print("=" * 60)
    print("      CONSULTORIO ODONTOLOGICO - MENU PRINCIPAL")
    print("=" * 60)
    print("    1.  Registrar nuevo paciente")
    print("    2.  Mostrar todos los pacientes")
    print("    3.  Mostrar citas por fechas proximas")
    print("    4.  Mostrar estadisticas del consultorio")
    print("    5.  Ordenar pacientes por valor (Mayor a Menor)")
    print("    6.  Buscar paciente por documento")
    print("    7.  Buscar paciente por valor (Busqueda Binaria)")
    print("    8.  Filtrar pacientes por tipo de cliente")
    print("    9.  Filtrar pacientes por tipo de atencion")
    print("    10. Salir")
    print("=" * 60)


def menu_principal():
    consultorio = Consultorio()

    print()
    print("  " + "*" * 54)
    print("  *                                                    *")
    print("  *     SISTEMA DE GESTION - CONSULTORIO ODONTOLOGICO  *")
    print("  *     Programacion 2 - Universidad de Manizales      *")
    print("  *     Nicolas David Solano Plazas                     *")
    print("  *                                                    *")
    print("  " + "*" * 54)
    print()

    cargar_datos_de_prueba(consultorio)
    print()

    while True:
        mostrar_menu()
        opcion = input("    Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_cliente_por_consola(consultorio)

        elif opcion == "2":
            consultorio.mostrar_clientes()

        elif opcion == "3":
            consultorio.mostrar_citas_proximas()

        elif opcion == "4":
            consultorio.mostrar_estadisticas()

        elif opcion == "5":
            consultorio.ordenar_clientes_por_valor()
            consultorio.mostrar_clientes()

        elif opcion == "6":
            cedula = input("\n  Ingrese el documento a buscar: ").strip()
            consultorio.buscar_cliente_por_cedula(cedula)

        elif opcion == "7":
            if len(consultorio.clientes) == 0:
                print("\n  No hay pacientes registrados.\n")
            else:
                consultorio.ordenar_clientes_por_valor()
                try:
                    valor = int(input("\n  Ingrese el valor a buscar: ").strip())
                    consultorio.buscar_cliente_por_valor(valor)
                except ValueError:
                    print("  Debe ingresar un valor numerico.\n")

        elif opcion == "8":
            tipo = leer_opcion_valida(
                "\n  Tipo de paciente (particular / eps / prepagada): ",
                ["particular", "eps", "prepagada"]
            )
            consultorio.filtrar_por_tipo_cliente(tipo)

        elif opcion == "9":
            tipo = leer_opcion_valida(
                "\n  Tipo de atencion (limpieza / calzas / extraccion / diagnostico): ",
                ["limpieza", "calzas", "extraccion", "diagnostico"]
            )
            consultorio.filtrar_por_tipo_atencion(tipo)

        elif opcion == "10":
            print("\n  Gracias por usar el sistema. Hasta pronto.\n")
            break

        else:
            print("\n  Opcion no valida. Intente de nuevo.\n")


if __name__ == "__main__":
    menu_principal()