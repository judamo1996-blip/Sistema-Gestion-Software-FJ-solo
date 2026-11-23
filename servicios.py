
from abc import ABC, abstractmethod


class Servicio(ABC):
    """Clase abstracta que representa un servicio de Software FJ."""

    def __init__(self, tarifa):
        if isinstance(tarifa, bool) or not isinstance(tarifa, (int, float)):
            raise ValueError("La tarifa debe ser un valor numérico.")

        if tarifa <= 0:
            raise ValueError("La tarifa debe ser mayor a cero.")

        self.__tarifa = tarifa
        self.__disponible = True

    @property
    def tarifa(self):
        """Permite consultar la tarifa sin modificarla directamente."""
        return self.__tarifa

    @property
    def disponible(self):
        """Permite consultar la disponibilidad del servicio."""
        return self.__disponible

    @disponible.setter
    def disponible(self, valor):
        """Permite modificar la disponibilidad de forma controlada."""
        if not isinstance(valor, bool):
            raise ValueError("La disponibilidad debe ser verdadera o falsa.")

        self.__disponible = valor

    def validar_duracion(self, duracion):
        """Valida la duración utilizada para calcular el costo."""
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
            raise ValueError("La duración debe ser un valor numérico.")

        if duracion <= 0:
            raise ValueError("La duración debe ser mayor a cero.")

    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass


class ReservaSala(Servicio):
    """Servicio de reserva de salas."""

    def __init__(self, sala, tarifa):
        if not isinstance(sala, str):
            raise ValueError("El nombre de la sala debe ser un texto.")

        if not sala.strip():
            raise ValueError("El nombre de la sala no puede estar vacío.")

        super().__init__(tarifa)
        self.__sala = sala.strip()

    @property
    def sala(self):
        return self.__sala

    def calcular_costo(self, duracion):
        self.validar_duracion(duracion)
        return self.tarifa * duracion

    def describir_servicio(self):
        return (
            f"Reserva de sala: {self.sala}, "
            f"tarifa por hora: ${self.tarifa}"
        )


class AlquilerEquipo(Servicio):
    """Servicio de alquiler de equipos."""

    def __init__(self, equipo, tarifa):
        if not isinstance(equipo, str):
            raise ValueError("El nombre del equipo debe ser un texto.")

        if not equipo.strip():
            raise ValueError("El nombre del equipo no puede estar vacío.")

        super().__init__(tarifa)
        self.__equipo = equipo.strip()

    @property
    def equipo(self):
        return self.__equipo

    def calcular_costo(self, duracion):
        self.validar_duracion(duracion)
        return self.tarifa * duracion

    def describir_servicio(self):
        return (
            f"Alquiler de equipo: {self.equipo}, "
            f"tarifa por hora: ${self.tarifa}"
        )


class AsesoriaEspecializada(Servicio):
    """Servicio de asesoría especializada."""

    def __init__(self, asesor, tarifa):
        if not isinstance(asesor, str):
            raise ValueError("El nombre del asesor debe ser un texto.")

        if not asesor.strip():
            raise ValueError("El nombre del asesor no puede estar vacío.")

        super().__init__(tarifa)
        self.__asesor = asesor.strip()

    @property
    def asesor(self):
        return self.__asesor

    def calcular_costo(self, duracion):
        self.validar_duracion(duracion)
        return self.tarifa * duracion

    def describir_servicio(self):
        return (
            f"Asesoría especializada: {self.asesor}, "
            f"tarifa por hora: ${self.tarifa}"
        )
