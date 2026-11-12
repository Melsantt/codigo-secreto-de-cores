
def validar_rgb(r, g, b):

    canais = [r, g, b]

    for canal in canais:
        if not isinstance(canal, int):
            return False

        if canal < 0 or canal > 255:
            return False

    return True


def validar_hex(hexadecimal):

    hexadecimal = hexadecimal.replace("#", "")

    if len(hexadecimal) != 6:
        return False

    try:
        int(hexadecimal, 16)
        return True

    except ValueError:
        return False


def validar_binario(binario):

    canais = binario.split()

    if len(canais) != 3:
        return False

    for canal in canais:
        if len(canal) != 8:
            return False

        if any(digito not in "01" for digito in canal):
            return False

    return True


def validar_hex(hexadecimal):

    # Remove o # caso esteja presente
    hexadecimal = hexadecimal.replace("#", "")

    # Verifica se possui exatamente 6 caracteres
    if len(hexadecimal) != 6:
        return False

    # Verifica se todos os caracteres são hexadecimais
    try:
        int(hexadecimal, 16)
        return True

    except ValueError:
        return False


def validar_binario(binario):

    # Separa os três canais binários
    partes = binario.split()

    # Verifica se existem exatamente três canais
    if len(partes) != 3:
        return False

    # Verifica se cada canal possui exatamente 8 dígitos
    for parte in partes:

        if len(parte) != 8:
            return False

        # Verifica se contém apenas 0 e 1
        if any(digito not in "01" for digito in parte):
            return False

    return True
