
def rgb_para_hex(r, g, b):
    vermelho = format(r, '02X')
    verde = format(g, '02X')
    azul = format(b, '02X')

    return f"#{vermelho}{verde}{azul}"


def rgb_para_binario(r, g, b):
    vermelho = format(r, '08b')
    verde = format(g, '08b')
    azul = format(b, '08b')

    return f"{vermelho} {verde} {azul}"


def hex_para_rgb(hexadecimal):
    hexadecimal = hexadecimal.replace("#", "")

    vermelho = int(hexadecimal[0:2], 16)
    verde = int(hexadecimal[2:4], 16)
    azul = int(hexadecimal[4:6], 16)

    return vermelho, verde, azul


def binario_para_rgb(binario):
    canais = binario.split()

    vermelho = int(canais[0], 2)
    verde = int(canais[1], 2)
    azul = int(canais[2], 2)

    return vermelho, verde, azul


def hex_para_rgb(hexadecimal):

    # Remove o # caso esteja presente
    hexadecimal = hexadecimal.replace("#", "")

    # Separa o código hexadecimal em três partes
    vermelho = hexadecimal[0:2]
    verde = hexadecimal[2:4]
    azul = hexadecimal[4:6]

    # Converte cada parte hexadecimal para decimal
    vermelho = int(vermelho, 16)
    verde = int(verde, 16)
    azul = int(azul, 16)

    # Retorna os três valores RGB
    return vermelho, verde, azul


def binario_para_rgb(binario):

    # Separa os três canais binários
    vermelho, verde, azul = binario.split()

    # Converte cada canal binário para decimal
    vermelho = int(vermelho, 2)
    verde = int(verde, 2)
    azul = int(azul, 2)

    # Retorna os valores RGB
    return vermelho, verde, azul
