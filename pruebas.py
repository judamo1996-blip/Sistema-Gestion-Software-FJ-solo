
from datetime import date

from clientes import Cliente
from servicios import Servicio,ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from gestion import SistemaGestion
from registro import registrar_evento, registrar_error


sistema = SistemaGestion()


def ejecutar_prueba(nombre, operacion):
    """Ejecuta una prueba y captura cualquier error sin detener el programa."""

    print(f"\nPRUEBA: {nombre}")

    try:
        resultado = operacion()

    except Exception as error:
        registrar_error(f"Prueba fallida - {nombre}: {error}")
        print(f"Error controlado: {error}")
        return None

    else:
        registrar_evento(f"Prueba exitosa: {nombre}")
        print("Resultado: operación realizada correctamente.")
        return resultado

    finally:
        print("Finalizó la prueba.")


# --------------------------------------------------
# PRUEBA 1. Crear un cliente válido.
# --------------------------------------------------

cliente = ejecutar_prueba(
    "Crear cliente válido",
    lambda: Cliente(
        "Daniel",
        "Monsalve",
        "daniel@gmail.com",
        "3001234567"
    )
)


# --------------------------------------------------
# PRUEBA 2. Intentar crear un cliente con correo inválido.
# --------------------------------------------------

ejecutar_prueba(
    "Crear cliente con correo inválido",
    lambda: Cliente(
        "Carlos",
        "Perez",
        "correo incorrecto",
        "3001234567"
    )
)


# --------------------------------------------------
# PRUEBA 3. Registrar el cliente en el sistema.
# --------------------------------------------------

ejecutar_prueba(
    "Registrar cliente",
    lambda: sistema.registrar_cliente(cliente)
)


# --------------------------------------------------
# PRUEBA 4. Crear un servicio válido.
# --------------------------------------------------

servicio = ejecutar_prueba(
    "Crear servicio de reserva de sala",
    lambda: ReservaSala("Sala principal", 20000)
)


# --------------------------------------------------
# PRUEBA 5. Intentar crear un servicio con tarifa inválida.
# --------------------------------------------------

ejecutar_prueba(
    "Crear servicio con tarifa negativa",
    lambda: ReservaSala("Sala secundaria", -5000)
)


# --------------------------------------------------
# PRUEBA 6. Registrar el servicio.
# --------------------------------------------------

ejecutar_prueba(
    "Registrar servicio",
    lambda: sistema.registrar_servicio(servicio)
)


# --------------------------------------------------
# PRUEBA 7. Crear una reservación correctamente.
# --------------------------------------------------

reservacion = ejecutar_prueba(
    "Crear reservación válida",
    lambda: sistema.crear_reservacion(
        cliente,
        servicio,
        date.today(),
        3
    )
)


# --------------------------------------------------
# PRUEBA 8. Intentar reservar con un cliente no registrado.
# --------------------------------------------------

cliente_no_registrado = Cliente(
    "Andres",
    "Lopez",
    "andres@gmail.com",
    "3111234567"
)

ejecutar_prueba(
    "Crear reservación con cliente no registrado",
    lambda: sistema.crear_reservacion(
        cliente_no_registrado,
        servicio,
        date.today(),
        2
    )
)


# --------------------------------------------------
# PRUEBA 9. Intentar reservar un servicio no disponible.
# --------------------------------------------------

servicio.disponible = False

ejecutar_prueba(
    "Crear reservación con servicio no disponible",
    lambda: sistema.crear_reservacion(
        cliente,
        servicio,
        date.today(),
        2
    )
)

servicio.disponible = True


# --------------------------------------------------
# PRUEBA 10. Confirmar una reservación.
# --------------------------------------------------

ejecutar_prueba(
    "Confirmar reservación",
    lambda: sistema.confirmar_reservacion(reservacion)
)


# --------------------------------------------------
# PRUEBA 11. Procesar una reservación confirmada.
# --------------------------------------------------

ejecutar_prueba(
    "Procesar reservación",
    lambda: sistema.procesar_reservacion(reservacion)
)


# --------------------------------------------------
# PRUEBA 12. Crear una segunda reservación.
# --------------------------------------------------

segunda_reservacion = ejecutar_prueba(
    "Crear segunda reservación",
    lambda: sistema.crear_reservacion(
        cliente,
        servicio,
        date.today(),
        2
    )
)


# --------------------------------------------------
# PRUEBA 13. Cancelar una reservación.
# --------------------------------------------------

ejecutar_prueba(
    "Cancelar reservación",
    lambda: sistema.cancelar_reservacion(segunda_reservacion)
)


# --------------------------------------------------
# PRUEBA 14. Intentar procesar una reservación cancelada.
# --------------------------------------------------

ejecutar_prueba(
    "Procesar reservación cancelada",
    lambda: sistema.procesar_reservacion(segunda_reservacion)
)


# --------------------------------------------------
# PRUEBA 15. Intentar registrar un estado inválido.
# --------------------------------------------------

ejecutar_prueba(
    "Cambiar a un estado no permitido",
    lambda: reservacion.cambiar_estado("finalizada")
)

# PRUEBA 16. Calcular costo sin descuento ni impuesto.
ejecutar_prueba(
    "Calcular costo sin ajustes",
    lambda: print(
        f"Costo: ${reservacion.calcular_costo_total()}"
    )
)

# PRUEBA 17. Calcular costo aplicando descuento.
ejecutar_prueba(
    "Calcular costo con descuento del 10%",
    lambda: print(
        f"Costo: ${reservacion.calcular_costo_total(descuento=10)}"
    )
)

# PRUEBA 18. Calcular costo con descuento e impuesto.
ejecutar_prueba(
    "Calcular costo con descuento e impuesto",
    lambda: print(
        f"Costo: ${reservacion.calcular_costo_total(descuento=10, impuesto=19)}"
    )
)

# PRUEBA 19. Crear alquiler de equipo.
ejecutar_prueba(
    "Crear servicio de alquiler de equipo",
    lambda: AlquilerEquipo("Computador portátil", 15000)
)

# PRUEBA 20. Crear asesoría especializada.
ejecutar_prueba(
    "Crear servicio de asesoría especializada",
    lambda: AsesoriaEspecializada("Carlos Pérez", 30000)
)

# PRUEBA 21. Comprobar el polimorfismo.

servicios_prueba = [
    ReservaSala("Sala de reuniones", 20000),
    AlquilerEquipo("Computador", 15000),
    AsesoriaEspecializada("Carlos Pérez", 30000)
]

for servicio_prueba in servicios_prueba:
    ejecutar_prueba(
        f"Polimorfismo: {type(servicio_prueba).__name__}",
        lambda s=servicio_prueba: (
            print(s.describir_servicio()),
            print(f"Costo por 2 horas: ${s.calcular_costo(2)}")
        )
    )
# --------------------------------------------------
# RESUMEN FINAL
# --------------------------------------------------

print("\n===================================")
print("       RESUMEN DE LAS PRUEBAS")
print("===================================")

print(f"Clientes registrados: {len(sistema.clientes)}")
print(f"Servicios registrados: {len(sistema.servicios)}")
print(f"Reservaciones creadas: {len(sistema.reservaciones)}")

print("\nRevisa el archivo software_fj.log")
print("para consultar los eventos y errores.")

registrar_evento("Finalizaron las pruebas del sistema Software FJ.")

print("\nPruebas finalizadas.")
