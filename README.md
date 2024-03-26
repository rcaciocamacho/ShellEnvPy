# Gestor de Entornos Virtuales de Python

> Este script en Python permite gestionar entornos virtuales de Python en sistemas operativos Windows.
> Proporciona opciones para crear, activar, desactivar y eliminar entornos virtuales.

## Uso

El script se ejecuta desde la línea de comandos con las siguientes opciones:

- `crear`: Crea un nuevo entorno virtual.
- `activar`: Activa un entorno virtual existente.
- `desactivar`: Desactiva el entorno virtual activo.
- `eliminar`: Elimina un entorno virtual existente.

## Opciones

- `-n, --nombre`: Especifica el nombre del entorno virtual.

## Ejemplos de Uso

```bash
python gestor_entornos.py crear -n nombre_entorno
python gestor_entornos.py activar -n nombre_entorno
python gestor_entornos.py desactivar
python gestor_entornos.py eliminar -n nombre_entorno
```

## Requisitos

> Python 3.x instalado en el sistema.
> Módulo virtualenv instalado (pip install virtualenv).
