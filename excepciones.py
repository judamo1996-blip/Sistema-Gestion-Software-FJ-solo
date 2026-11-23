class ErrorSistema(Exception):
    """Error general del sistema Software FJ."""
    pass


class ErrorValidacion(ErrorSistema):
    """Error cuando los datos no cumplen las condiciones."""
    pass


class ErrorOperacion(ErrorSistema):
    """Error cuando una operación no está permitida."""
    pass


class ErrorReserva(ErrorSistema):
    """Error relacionado con las reservaciones."""
    pass


class ServicioNoDisponible(ErrorSistema):
    """Error cuando un servicio no está disponible."""
    pass
