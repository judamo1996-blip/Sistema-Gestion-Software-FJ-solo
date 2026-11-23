
from datetime import date
from clientes import Cliente
from servicios import Servicio


class Reservacion:
    """Representa una reservación de un servicio de Software FJ."""

    def __init__(self, cliente, servicio, fecha, duracion):

        if not isinstance(cliente, Cliente):
            raise ValueError("Debe proporcionar un cliente válido.")

        if not isinstance(servicio, Servicio):
            raise ValueError("Debe proporcionar un servicio válido.")

        if not isinstance(fecha, date):
            raise ValueError("La fecha debe ser una instancia de date.")

        self.__cliente = cliente
        self.__servicio = servicio
        self.__fecha = fecha
        self.__duracion = duracion
        self.__estado = "pendiente"

        self.validar_duracion(duracion)

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def fecha(self):
        return self.__fecha

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    def validar_duracion(self, duracion):
        """Comprueba que la duración sea válida."""

        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
            raise ValueError("La duración debe ser un valor numérico.")

        if duracion <= 0:
            raise ValueError("La duración debe ser mayor a cero.")

    def calcular_costo_total(self, descuento=0, impuesto=0):
        """Calcula el costo con descuentos e impuestos opcionales."""

        if isinstance(descuento, bool) or not isinstance(descuento, (int, float)):
            raise ValueError("El descuento debe ser numérico.")

        if isinstance(impuesto, bool) or not isinstance(impuesto, (int, float)):
            raise ValueError("El impuesto debe ser numérico.")

        if not 0 <= descuento <= 100:
            raise ValueError("El descuento debe estar entre 0 y 100.")

        if not 0 <= impuesto <= 100:
            raise ValueError("El impuesto debe estar entre 0 y 100.")

        subtotal = self.__servicio.calcular_costo(self.__duracion)

        valor_descuento = subtotal * (descuento / 100)
        total_con_descuento = subtotal - valor_descuento

        valor_impuesto = total_con_descuento * (impuesto / 100)

        return total_con_descuento + valor_impuesto

    def cambiar_estado(self, nuevo_estado):
        """Modifica el estado después de validar las condiciones."""

        estados_validos = ["pendiente", "confirmada", "cancelada"]

        if not isinstance(nuevo_estado, str):
            raise ValueError("El estado debe ser un texto válido.")

        nuevo_estado = nuevo_estado.strip().lower()

        if nuevo_estado not in estados_validos:
            raise ValueError(
                "El estado debe ser pendiente, confirmada o cancelada."
            )

        if self.__estado == "cancelada":
            raise ValueError(
                "No se puede cambiar el estado de una reservación cancelada."
            )

        if self.__estado == "confirmada" and nuevo_estado == "pendiente":
            raise ValueError(
                "No se puede cambiar una reservación confirmada a pendiente."
            )

        if self.__estado == nuevo_estado:
            raise ValueError("La reservación ya tiene ese estado.")

        self.__estado = nuevo_estado

    def confirmar(self):
        """Confirma una reservación pendiente."""
        self.cambiar_estado("confirmada")

    def cancelar(self):
        """Cancela una reservación."""
        self.cambiar_estado("cancelada")

    def procesar(self):
        """Procesa una reservación que ya fue confirmada."""

        if self.__estado != "confirmada":
            raise ValueError(
                "Solo se pueden procesar reservaciones confirmadas."
            )

        return self.calcular_costo_total()

    def mostrar_informacion(self):
        """Devuelve un resumen de la reservación."""

        return (
            f"Cliente: {self.__cliente.mostrar_informacion()}\n"
            f"Servicio: {self.__servicio.describir_servicio()}\n"
            f"Fecha: {self.__fecha}\n"
            f"Duración: {self.__duracion} horas\n"
            f"Estado: {self.__estado}\n"
            f"Costo: ${self.calcular_costo_total()}"
        )
