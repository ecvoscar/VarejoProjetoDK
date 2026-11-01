# Formatação dados console números Brasil

import rich.console

console = rich.console.Console()

def numero_br(valor, casas=0):
    texto = f"{valor:,.{casas}f}"
    texto = texto.replace(",", "X")
    texto = texto.replace(".", ",")
    texto = texto.replace("X", ".")
    return texto