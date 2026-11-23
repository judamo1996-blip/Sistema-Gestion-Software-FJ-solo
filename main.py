
from datetime import date
from clientes import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from gestion import SistemaGestion
from registro import registrar_evento, registrar_error, registrar_advertencia


sistema = SistemaGestion()


def mostrar_menu():
    print("\n===================================")
    print("       SISTEMA SOFTWARE FJ")
    print("===================================")
    print("1. Registrar cliente")
    print("2. Registrar servicio")
    print("3. Crear reservación")
    print("4. Confirmar reservación")
    print("5. Cancelar reservación")
    print("6. Procesar reservación")
    print("7. Consultar clientes")
    print("8. Consultar servicios")
    print("9. Consultar reservaciones")
    print("0. Salir")
    print("===================================")


def seleccionar_reservacion():
    if not sistema.reservaciones:
        print("No existen reservaciones registradas.")
        return None

    for indice, reservacion in enumerate(sistema.reservaciones, start=1):
        print(
            f"{indice}. {reservacion.cliente.mostrar_informacion()} "
            f"| Estado: {reservacion.estado}"
        )

    try:
        opcion = int(input("Seleccione el número de reservación: "))

        if opcion < 1 or opcion > len(sistema.reservaciones):
            raise ValueError("Número de reservación fuera de rango.")

        return sistema.reservaciones[opcion - 1]

    except ValueError as error:
        registrar_advertencia(f"Selección de reservación inválida: {error}")
        print(f"Selección incorrecta: {error}")
        return None


def ejecutar_sistema():
    while True:
        mostrar_menu()

        try:
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                correo = input("Correo: ")
                telefono = input("Teléfono: ")

                cliente = Cliente(nombre, apellido, correo, telefono)
                sistema.registrar_cliente(cliente)

                print("Cliente registrado correctamente.")

            elif opcion == "2":
                print("\nTipos de servicio:")
                print("1. Reserva de sala")
                print("2. Alquiler de equipo")
                print("3. Asesoría especializada")

                tipo = input("Seleccione el tipo: ").strip()
                tarifa = float(input("Tarifa por hora: "))

                if tipo == "1":
                    nombre = input("Nombre de la sala: ")
                    servicio = ReservaSala(nombre, tarifa)

                elif tipo == "2":
                    nombre = input("Nombre del equipo: ")
                    servicio = AlquilerEquipo(nombre, tarifa)

                elif tipo == "3":
                    nombre = input("Nombre del asesor: ")
                    servicio = AsesoriaEspecializada(nombre, tarifa)

                else:
                    raise ValueError("Tipo de servicio no válido.")

                sistema.registrar_servicio(servicio)
                print("Servicio registrado correctamente.")

            elif opcion == "3":
                if not sistema.clientes or not sistema.servicios:
                    raise ValueError(
                        "Primero debe registrar clientes y servicios."
                    )

                print("\nClientes:")
                for indice, cliente in enumerate(sistema.clientes, start=1):
                    print(f"{indice}. {cliente.mostrar_informacion()}")

                cliente_numero = int(input("Seleccione el cliente: "))

                if not 1 <= cliente_numero <= len(sistema.clientes):
                    raise ValueError("Cliente seleccionado no válido.")

                print("\nServicios:")
                for indice, servicio in enumerate(sistema.servicios, start=1):
                    print(f"{indice}. {servicio.describir_servicio()}")

                servicio_numero = int(input("Seleccione el servicio: "))

                if not 1 <= servicio_numero <= len(sistema.servicios):
                    raise ValueError("Servicio seleccionado no válido.")

                duracion = float(input("Duración en horas: "))

                reservacion = sistema.crear_reservacion(
                    sistema.clientes[cliente_numero - 1],
                    sistema.servicios[servicio_numero - 1],
                    date.today(),
                    duracion
                )

                print("Reservación creada correctamente.")
                print(reservacion.mostrar_informacion())

            elif opcion == "4":
                reservacion = seleccionar_reservacion()
                if reservacion:
                    sistema.confirmar_reservacion(reservacion)
                    print("Reservación confirmada.")

            elif opcion == "5":
                reservacion = seleccionar_reservacion()
                if reservacion:
                    sistema.cancelar_reservacion(reservacion)
                    print("Reservación cancelada.")

            elif opcion == "6":
                reservacion = seleccionar_reservacion()
                if reservacion:
                    costo = sistema.procesar_reservacion(reservacion)
                    print(f"Reservación procesada. Total: ${costo:,.2f}")

            elif opcion == "7":
                print("\nCLIENTES REGISTRADOS")
                for cliente in sistema.listar_clientes():
                    print(cliente)

            elif opcion == "8":
                print("\nSERVICIOS REGISTRADOS")
                for servicio in sistema.listar_servicios():
                    print(servicio)

            elif opcion == "9":
                print("\nRESERVACIONES REGISTRADAS")
                for reservacion in sistema.listar_reservaciones():
                    print(reservacion.mostrar_informacion())
                    print("-----------------------------------")

            elif opcion == "0":
                registrar_evento("El usuario cerró el sistema.")
                print("Gracias por utilizar Software FJ.")
                break

            else:
                raise ValueError("La opción seleccionada no existe.")

        except Exception as error:
            registrar_error(f"Error durante la ejecución del menú: {error}")
            print(f"\nNo se pudo completar la operación: {error}")
            print("El sistema continúa funcionando.")

        finally:
            print("\nOperación finalizada.")


if __name__ == "__main__":
    ejecutar_sistema()
