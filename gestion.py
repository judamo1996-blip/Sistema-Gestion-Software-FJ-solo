
from clientes import Cliente
from servicios import Servicio
from reservas import Reservacion

from excepciones import (
    ErrorValidacion,
    ErrorReserva,
    ErrorOperacion,
    ServicioNoDisponible
)

from registro import (
    registrar_evento,
    registrar_error,
    registrar_advertencia
)


class SistemaGestion:
    """Administra clientes, servicios y reservaciones de Software FJ."""

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservaciones = []

    def registrar_cliente(self, cliente):
        try:
            if not isinstance(cliente, Cliente):
                raise TypeError("El objeto debe ser un cliente válido.")

            if cliente in self.clientes:
                raise ValueError("El cliente ya está registrado.")

            self.clientes.append(cliente)

        except Exception as error:
            registrar_error(f"Error al registrar cliente: {error}")
            raise ErrorValidacion(
                "No fue posible registrar el cliente."
            ) from error

        else:
            registrar_evento("Cliente registrado correctamente.")

        finally:
            registrar_evento(
                "Finalizó el intento de registro de cliente."
            )

    def registrar_servicio(self, servicio):
        try:
            if not isinstance(servicio, Servicio):
                raise TypeError("El objeto debe ser un servicio válido.")

            if servicio in self.servicios:
                raise ValueError("El servicio ya está registrado.")

            self.servicios.append(servicio)

        except Exception as error:
            registrar_error(f"Error al registrar servicio: {error}")
            raise ErrorValidacion(
                "No fue posible registrar el servicio."
            ) from error

        else:
            registrar_evento("Servicio registrado correctamente.")

        finally:
            registrar_evento(
                "Finalizó el intento de registro de servicio."
            )

    def crear_reservacion(self, cliente, servicio, fecha, duracion):
        try:
            if cliente not in self.clientes:
                raise ValueError("El cliente no está registrado.")

            if servicio not in self.servicios:
                raise ValueError("El servicio no está registrado.")

            if not servicio.disponible:
                registrar_advertencia(
                    "Se intentó reservar un servicio no disponible."
                )
                raise ServicioNoDisponible(
                    "El servicio no se encuentra disponible."
                )

            reservacion = Reservacion(
                cliente, servicio, fecha, duracion
            )

            self.reservaciones.append(reservacion)

        except Exception as error:
            registrar_error(f"Error al crear reservación: {error}")
            raise ErrorReserva(
                "No fue posible crear la reservación."
            ) from error

        else:
            registrar_evento("Reservación creada correctamente.")
            return reservacion

        finally:
            registrar_evento(
                "Finalizó el intento de crear reservación."
            )

    def confirmar_reservacion(self, reservacion):
        try:
            if reservacion not in self.reservaciones:
                raise ValueError(
                    "La reservación no pertenece al sistema."
                )

            reservacion.confirmar()

        except Exception as error:
            registrar_error(
                f"Error al confirmar reservación: {error}"
            )
            raise ErrorOperacion(
                "No fue posible confirmar la reservación."
            ) from error

        else:
            registrar_evento(
                "Reservación confirmada correctamente."
            )

        finally:
            registrar_evento(
                "Finalizó el intento de confirmar reservación."
            )

    def cancelar_reservacion(self, reservacion):
        try:
            if reservacion not in self.reservaciones:
                raise ValueError(
                    "La reservación no pertenece al sistema."
                )

            reservacion.cancelar()

        except Exception as error:
            registrar_error(
                f"Error al cancelar reservación: {error}"
            )
            raise ErrorOperacion(
                "No fue posible cancelar la reservación."
            ) from error

        else:
            registrar_evento(
                "Reservación cancelada correctamente."
            )

        finally:
            registrar_evento(
                "Finalizó el intento de cancelar reservación."
            )

    def procesar_reservacion(self, reservacion):
        try:
            if reservacion not in self.reservaciones:
                raise ValueError(
                    "La reservación no pertenece al sistema."
                )

            costo = reservacion.procesar()

        except Exception as error:
            registrar_error(
                f"Error al procesar reservación: {error}"
            )
            raise ErrorReserva(
                "No fue posible procesar la reservación."
            ) from error

        else:
            registrar_evento(
                f"Reservación procesada. Costo total: ${costo}"
            )
            return costo

        finally:
            registrar_evento(
                "Finalizó el intento de procesar reservación."
            )

    def listar_clientes(self):
        return [
            cliente.mostrar_informacion()
            for cliente in self.clientes
        ]

    def listar_servicios(self):
        return [
            servicio.describir_servicio()
            for servicio in self.servicios
        ]

    def listar_reservaciones(self):
        return self.reservaciones.copy()
