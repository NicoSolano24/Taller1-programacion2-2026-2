# ===================================================================
# consultorio.py - Clase Consultorio
# ===================================================================
# Estudiante: Nicolas David Solano Plazas
# Código: 106202524246
# ===================================================================

from cliente import Cliente
from datetime import datetime


class Consultorio:
    """
    Clase que administra los clientes del consultorio odontologico.
    """

    def __init__(self):
        self.clientes = []

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def existe_cedula(self, cedula):
        for cliente in self.clientes:
            if cliente.cedula == cedula:
                return True
        return False

    def _calcular_anchos(self, lista_clientes):
        ancho_num = max(2, len(str(len(lista_clientes))))
        ancho_ced = len("Documento")
        ancho_nom = len("Nombre")
        ancho_tel = len("Telefono")
        ancho_cli = len("Tipo Cliente")
        ancho_ate = len("Atencion")
        ancho_can = len("Cant")
        ancho_pri = len("Prioridad")
        ancho_fec = len("Fecha")
        ancho_tot = len("Valor Total")

        for c in lista_clientes:
            ancho_ced = max(ancho_ced, len(c.cedula))
            ancho_nom = max(ancho_nom, len(c.nombre))
            ancho_tel = max(ancho_tel, len(c.telefono))
            ancho_cli = max(ancho_cli, len(c.tipo_cliente))
            ancho_ate = max(ancho_ate, len(c.tipo_atencion))
            ancho_can = max(ancho_can, len(str(c.cantidad)))
            ancho_pri = max(ancho_pri, len(c.prioridad_atencion))
            ancho_fec = max(ancho_fec, len(c.fecha_cita))
            ancho_tot = max(ancho_tot, len(f"${c.valor_total:,.0f}"))

        return (ancho_num, ancho_ced, ancho_nom, ancho_tel,
                ancho_cli, ancho_ate, ancho_can, ancho_pri,
                ancho_fec, ancho_tot)

    def _dibujar_tabla(self, lista_clientes, titulo):
        if len(lista_clientes) == 0:
            print("\n  No hay pacientes para mostrar.\n")
            return

        anchos = self._calcular_anchos(lista_clientes)
        (a_num, a_ced, a_nom, a_tel, a_cli, a_ate, a_can, a_pri, a_fec, a_tot) = anchos

        encabezado = (
            f"  {'#':<{a_num}} | "
            f"{'Documento':<{a_ced}} | "
            f"{'Nombre':<{a_nom}} | "
            f"{'Telefono':<{a_tel}} | "
            f"{'Tipo Cliente':<{a_cli}} | "
            f"{'Atencion':<{a_ate}} | "
            f"{'Cant':<{a_can}} | "
            f"{'Prioridad':<{a_pri}} | "
            f"{'Fecha':<{a_fec}} | "
            f"{'Valor Total':>{a_tot}}"
        )

        ancho_total = len(encabezado) + 2
        separador = "  " + "-" * (ancho_total - 2)

        print()
        print("  " + "=" * (ancho_total - 2))
        print(f"  {titulo}")
        print("  " + "=" * (ancho_total - 2))
        print(encabezado)
        print(separador)

        for i, c in enumerate(lista_clientes, 1):
            fila = (
                f"  {i:<{a_num}} | "
                f"{c.cedula:<{a_ced}} | "
                f"{c.nombre:<{a_nom}} | "
                f"{c.telefono:<{a_tel}} | "
                f"{c.tipo_cliente.capitalize():<{a_cli}} | "
                f"{c.tipo_atencion.capitalize():<{a_ate}} | "
                f"{c.cantidad:<{a_can}} | "
                f"{c.prioridad_atencion.capitalize():<{a_pri}} | "
                f"{c.fecha_cita:<{a_fec}} | "
                f"{'$' + f'{c.valor_total:,.0f}':>{a_tot}}"
            )
            print(fila)

        print("  " + "=" * (ancho_total - 2))
        print(f"  Total: {len(lista_clientes)} paciente(s)\n")

    def mostrar_clientes(self):
        self._dibujar_tabla(self.clientes, "LISTA DE PACIENTES REGISTRADOS")

    def mostrar_citas_proximas(self):
        """Muestra los clientes ordenados por la fecha de su cita."""
        if len(self.clientes) == 0:
            print("\n  No hay pacientes registrados.\n")
            return

        def obtener_fecha(cliente):
            try:
                # Intenta convertir el string DD-MM-AAAA a una fecha real para ordenar
                return datetime.strptime(cliente.fecha_cita, "%d-%m-%Y")
            except ValueError:
                # Si alguien metio un formato raro, lo manda al final
                return datetime.max

        clientes_ordenados_fecha = sorted(self.clientes, key=obtener_fecha)
        self._dibujar_tabla(clientes_ordenados_fecha, "CITAS ORGANIZADAS POR FECHA (PROXIMAS)")

    def mostrar_estadisticas(self):
        if len(self.clientes) == 0:
            print("\n  No hay pacientes registrados para calcular estadisticas.\n")
            return

        total_clientes = len(self.clientes)
        ingresos_totales = sum(c.valor_total for c in self.clientes)
        extracciones = sum(1 for c in self.clientes if c.tipo_atencion == "extraccion")

        particulares = sum(1 for c in self.clientes if c.tipo_cliente == "particular")
        eps = sum(1 for c in self.clientes if c.tipo_cliente == "eps")
        prepagada = sum(1 for c in self.clientes if c.tipo_cliente == "prepagada")

        limpiezas = sum(1 for c in self.clientes if c.tipo_atencion == "limpieza")
        calzas = sum(1 for c in self.clientes if c.tipo_atencion == "calzas")
        diagnosticos = sum(1 for c in self.clientes if c.tipo_atencion == "diagnostico")

        urgentes = sum(1 for c in self.clientes if c.prioridad_atencion == "urgente")

        cliente_mayor = max(self.clientes, key=lambda c: c.valor_total)
        cliente_menor = min(self.clientes, key=lambda c: c.valor_total)

        print("\n" + "=" * 58)
        print("  ESTADISTICAS DEL CONSULTORIO")
        print("=" * 58)

        print(f"  Total de pacientes:             {total_clientes}")
        print(f"  Ingresos totales recibidos:     ${ingresos_totales:,.0f}")
        print(f"  Pacientes para extraccion:      {extracciones}")

        print("-" * 58)
        print("  DESGLOSE POR TIPO DE PACIENTE")
        print("-" * 58)
        print(f"  Particulares:                   {particulares}")
        print(f"  EPS:                            {eps}")
        print(f"  Prepagada:                      {prepagada}")

        print("-" * 58)
        print("  DESGLOSE POR TIPO DE ATENCION")
        print("-" * 58)
        print(f"  Limpieza:                       {limpiezas}")
        print(f"  Calzas:                         {calzas}")
        print(f"  Extraccion:                     {extracciones}")
        print(f"  Diagnostico:                    {diagnosticos}")

        print("-" * 58)
        print("  OTROS DATOS")
        print("-" * 58)
        print(f"  Pacientes urgentes:             {urgentes}")
        print(f"  Paciente con mayor valor:       {cliente_mayor.nombre} (${cliente_mayor.valor_total:,.0f})")
        print(f"  Paciente con menor valor:       {cliente_menor.nombre} (${cliente_menor.valor_total:,.0f})")
        print("=" * 58 + "\n")

    def ordenar_clientes_por_valor(self):
        self.clientes = self._quicksort(self.clientes)
        print("\n  Lista ordenada por valor de atencion (Mayor a Menor) usando QuickSort.")

    def _quicksort(self, lista):
        if len(lista) <= 1:
            return lista

        pivote = lista[0]

        mayores = [x for x in lista[1:] if x.valor_total >= pivote.valor_total]
        menores = [x for x in lista[1:] if x.valor_total < pivote.valor_total]

        return self._quicksort(mayores) + [pivote] + self._quicksort(menores)

    def buscar_cliente_por_cedula(self, cedula):
        print(f"\n  Buscando documento: {cedula} (Busqueda Secuencial)...")

        for cliente in self.clientes:
            if cliente.cedula == cedula:
                print("  Paciente encontrado!")
                self._mostrar_detalle_cliente(cliente)
                return cliente

        print("  Paciente no encontrado en el sistema.\n")
        return None

    def buscar_cliente_por_valor(self, valor_buscado):
        print(f"\n  Buscando pacientes con valor ${valor_buscado:,.0f} (Busqueda Binaria)...")

        inicio = 0
        fin = len(self.clientes) - 1
        encontrado = False

        while inicio <= fin:
            medio = (inicio + fin) // 2
            valor_medio = self.clientes[medio].valor_total

            if valor_medio == valor_buscado:
                print("  Paciente encontrado!")
                self._mostrar_detalle_cliente(self.clientes[medio])
                encontrado = True
                break
            elif valor_medio > valor_buscado:
                inicio = medio + 1
            else:
                fin = medio - 1

        if not encontrado:
            print("  No se encontro ningun paciente con ese valor.\n")

    def _mostrar_detalle_cliente(self, cliente):
        valor_cita, valor_atencion = cliente.obtener_desglose()

        print()
        print("  " + "+" + "-" * 44 + "+")
        print("  " + "|" + "  DETALLE DEL PACIENTE".center(44) + "|")
        print("  " + "+" + "-" * 44 + "+")
        print(f"  |  Documento:   {cliente.cedula:<26} |")
        print(f"  |  Nombre:      {cliente.nombre:<26} |")
        print(f"  |  Telefono:    {cliente.telefono:<26} |")
        print(f"  |  Tipo:        {cliente.tipo_cliente.capitalize():<26} |")
        print(f"  |  Atencion:    {cliente.tipo_atencion.capitalize():<26} |")
        print(f"  |  Cantidad:    {cliente.cantidad:<26} |")
        print(f"  |  Prioridad:   {cliente.prioridad_atencion.capitalize():<26} |")
        print(f"  |  Fecha cita:  {cliente.fecha_cita:<26} |")
        print("  " + "+" + "-" * 44 + "+")
        print(f"  |  Valor cita:          ${valor_cita:>14,.0f}   |")
        print(f"  |  Valor atencion:      ${valor_atencion:>14,.0f}   |")
        print(f"  |  Cantidad:            {cliente.cantidad:>15}   |")
        print(f"  |  Atencion x Cantidad: ${valor_atencion * cliente.cantidad:>14,.0f}   |")
        print("  " + "|" + "-" * 44 + "|")
        print(f"  |  TOTAL A PAGAR:       ${cliente.valor_total:>14,.0f}   |")
        print("  " + "+" + "-" * 44 + "+")
        print()

    def filtrar_por_tipo_cliente(self, tipo):
        filtrados = [c for c in self.clientes if c.tipo_cliente == tipo]
        titulo = f"PACIENTES TIPO: {tipo.upper()}"
        self._dibujar_tabla(filtrados, titulo)

    def filtrar_por_tipo_atencion(self, tipo):
        filtrados = [c for c in self.clientes if c.tipo_atencion == tipo]
        titulo = f"PACIENTES CON ATENCION: {tipo.upper()}"
        self._dibujar_tabla(filtrados, titulo)
