#!/bin/bash

# Verificar se o Homebrew está instalado
if ! command -v brew &> /dev/null
then
    echo "Homebrew não está instalado. Instalando Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "Homebrew já está instalado."
fi

# Verificar se o Python está instalado
if ! command -v python3 &> /dev/null
then
    echo "Python3 não está instalado. Instalando Python..."
    brew install python
else
    echo "Python3 já está instalado."
fi

# Rodar o script Python para continuar a configuração
# python3 install_apps
