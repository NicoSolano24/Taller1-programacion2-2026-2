# Taller 1 - Consultorio Odontológico

**Programación 2** - Universidad de Manizales (2026-2)  
**Estudiante:** Nicolas David Solano Plazas  
**Código:** 106202524246  
**Fecha:** Septiembre 2026

---

## Descripción del proyecto

Este es mi programa en Python para administrar las citas de un consultorio odontológico. El sistema sirve para registrar los datos de los pacientes, calcular automáticamente cuánto deben pagar dependiendo de si son particulares, de EPS o prepagada, y el tipo de procedimiento que se van a hacer. También le agregué funciones para ordenar la lista, buscar pacientes y ver estadísticas.

Para organizar mejor el código y aplicar buenas prácticas, dividí el proyecto en varios archivos. Así es más fácil de leer y mantener:

*   **`cliente.py`**: Aquí está la clase que representa al paciente. Se encarga de guardar sus datos y tiene la lógica para calcular cuánto cuesta su cita según la tabla de tarifas.
*   **`consultorio.py`**: Es como el cerebro del programa. Guarda la lista de pacientes y tiene los algoritmos para ordenarlos (usé QuickSort), buscarlos, organizarlos por fecha y generar las tablas dinámicas en consola.
*   **`utilidades.py`**: Aquí puse las funciones que interactúan con el usuario, como los menús para pedir datos, validar que escriban bien el teléfono o el documento, y cargar unos datos de prueba.
*   **`main.py`**: Es el archivo principal que arranca el programa y muestra el menú de opciones.

## Funcionalidades principales

- **Registrar clientes**: Pide los datos por consola. Valida que no se repitan documentos, que el documento pueda ser cédula o tarjeta de identidad, y que los teléfonos tengan exactamente 10 dígitos.
- **Cálculo de tarifas**: Aplica los precios según los requisitos del taller.
- **Tabla dinámica**: Las tablas se ajustan solas al tamaño de los nombres para que la información no se descuadre, sin importar si el nombre es muy largo.
- **Citas próximas**: Permite ver la lista de pacientes organizada por la fecha de su cita.
- **Estadísticas**: Muestra el total de clientes, el dinero que ingresó, cuántas extracciones hay, y un desglose mucho más detallado de la información.
- **Ordenar clientes**: Organiza de mayor a menor valor usando el algoritmo **QuickSort**.
- **Búsqueda**: Se puede buscar un paciente por su documento (búsqueda secuencial) o buscar por valor a pagar (búsqueda binaria).
- **Factura detallada**: Al buscar a alguien, muestra un resumen del paciente y de por qué se le cobra ese valor.

## Cómo probar el programa

1. Abre la terminal en la carpeta del proyecto.
2. Ejecuta el archivo principal con el comando:
   ```bash
   python main.py
   ```
3. El programa ya viene con unos pacientes de prueba cargados para que puedas probar las opciones de buscar, filtrar y ordenar sin tener que registrar todo desde cero.