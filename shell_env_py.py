import argparse
import subprocess
import os


def crear_entorno_virtual(nombre):
    try:
        # Crear el entorno virtual
        subprocess.run(["python", "-m", "venv", nombre], check=True)
        print(f"Entorno virtual '{nombre}' creado correctamente.")
    except subprocess.CalledProcessError:
        print(f"Error al crear el entorno virtual '{nombre}'.")


def activar_entorno_virtual(nombre):
    try:
        # Activar el entorno virtual
        comando_activacion = f"{nombre}\\Scripts\\activate"
        subprocess.run(comando_activacion, shell=True, check=True)
        print(f"Entorno virtual '{nombre}' activado.")
    except subprocess.CalledProcessError:
        print(f"Error al activar el entorno virtual '{nombre}'.")


def desactivar_entorno_virtual():
    # Desactivar el entorno virtual
    subprocess.run(["deactivate"], shell=True)


def eliminar_entorno_virtual(nombre):
    try:
        # Desactivar el entorno virtual si está activo
        desactivar_entorno_virtual()
        # Eliminar el entorno virtual
        os.system(f"rd /s /q {nombre}")
        print(f"Entorno virtual '{nombre}' eliminado correctamente.")
    except Exception as e:
        print(f"Error al eliminar el entorno virtual '{nombre}': {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Gestión de entornos virtuales de Python en Windows."
    )
    parser.add_argument(
        "opcion",
        choices=["crear", "activar", "desactivar", "eliminar"],
        help="Opción a ejecutar",
    )
    parser.add_argument("-n", "--nombre", help="Nombre del entorno virtual")

    args = parser.parse_args()

    if args.opcion == "crear":
        if args.nombre:
            crear_entorno_virtual(args.nombre)
        else:
            print("Debe especificar el nombre del entorno virtual.")
    elif args.opcion == "activar":
        if args.nombre:
            activar_entorno_virtual(args.nombre)
        else:
            print("Debe especificar el nombre del entorno virtual.")
    elif args.opcion == "desactivar":
        desactivar_entorno_virtual()
    elif args.opcion == "eliminar":
        if args.nombre:
            eliminar_entorno_virtual(args.nombre)
        else:
            print("Debe especificar el nombre del entorno virtual.")
