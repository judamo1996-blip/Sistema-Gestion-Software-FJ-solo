import logging

# Configuración del registro de eventos y errores.
logging.basicConfig(
    filename="software_fj.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Creamos un registrador para Software FJ.
logger = logging.getLogger("SoftwareFJ")


def registrar_evento(mensaje):
    """Registra una operación exitosa."""
    logger.info(mensaje)


def registrar_error(mensaje):
    """Registra un error del sistema."""
    logger.error(mensaje)


def registrar_advertencia(mensaje):
    """Registra una situación que requiere atención."""
    logger.warning(mensaje)