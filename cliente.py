# ===================================================================
# cliente.py - Clase Cliente
# ===================================================================
# Estudiante: Nicolas David Solano Plazas
# Código: 106202524246
# ===================================================================

class Cliente:
    """
    Representa a un cliente del consultorio odontologico.
    """

    TARIFAS = {
        "particular": {
            "valor_cita": 80000,
            "limpieza": 60000,
            "calzas": 80000,
            "extraccion": 100000,
            "diagnostico": 50000
        },
        "eps": {
            "valor_cita": 5000,
            "limpieza": 0,
            "calzas": 40000,
            "extraccion": 40000,
            "diagnostico": 0
        },
        "prepagada": {
            "valor_cita": 30000,
            "limpieza": 0,
            "calzas": 10000,
            "extraccion": 10000,
            "diagnostico": 0
        }
    }

    def __init__(self, cedula, nombre, telefono, tipo_cliente, tipo_atencion, cantidad, prioridad_atencion, fecha_cita):
        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono
        self.tipo_cliente = tipo_cliente.lower()
        self.tipo_atencion = tipo_atencion.lower()
        self.prioridad_atencion = prioridad_atencion.lower()
        self.fecha_cita = fecha_cita

        if self.tipo_atencion in ["limpieza", "diagnostico"]:
            self.cantidad = 1
        else:
            self.cantidad = cantidad if cantidad > 0 else 1

        self.valor_total = self.calcular_valor_servicio()

    def calcular_valor_servicio(self):
        tarifa = self.TARIFAS.get(self.tipo_cliente, {})
        valor_cita = tarifa.get("valor_cita", 0)
        valor_atencion = tarifa.get(self.tipo_atencion, 0)

        return valor_cita + (valor_atencion * self.cantidad)

    def obtener_desglose(self):
        tarifa = self.TARIFAS.get(self.tipo_cliente, {})
        valor_cita = tarifa.get("valor_cita", 0)
        valor_atencion = tarifa.get(self.tipo_atencion, 0)
        return valor_cita, valor_atencion
