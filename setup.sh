#!/bin/bash

# Directorio de destino
destino="$HOME/.config/shellEnvPy"

# Crear el directorio de destino si no existe
mkdir -p "$destino"

# Mover el script Python al directorio de destino
cp shell_env_py.py "$destino/"

# Crear el alias en ~/.zshrc
echo "alias envy='$destino/shell_env_py.py'" >> ~/.zshrc

# Recargar la configuración de la shell Zsh
source ~/.zshrc

echo "Instalación completada. Ahora puedes usar el comando 'envy' desde cualquier lugar."
