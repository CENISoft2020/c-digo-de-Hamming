def hamming_encode(data):
    # Calcula el número de bits de paridad necesarios (m)
    m = 0
    while 2**m < len(data) + m + 1:
        m += 1

    # Crea una lista de bits de paridad
    encoded_data = [0] * (len(data) + m)
    j = 0

    # Llena la lista de datos y bits de paridad
    for i in range(1, len(encoded_data) + 1):
        if i == 2**j:
            j += 1
        else:
            encoded_data[i - 1] = int(data.pop(0))

    j = 0

    # Calcula los bits de paridad
    for i in range(1, len(encoded_data) + 1):
        if i == 2**j:
            for k in range(i - 1, len(encoded_data), 2**j * 2):
                encoded_data[i - 1] ^= encoded_data[k]
            j += 1

    return encoded_data

def hamming_decode(encoded_data):
    m = 0
    while 2**m < len(encoded_data):
        m += 1

    error_position = 0

    # Calcula la posición del error
    for i in range(m):
        bit = 0
        for j in range(len(encoded_data)):
            if (j + 1) & (2**i):
                bit ^= encoded_data[j]
        error_position += bit * (2**i)

    # Corrige el error
    if error_position > 0:
        encoded_data[error_position - 1] ^= 1

    # Extrae los datos
    decoded_data = []
    j = 0

    for i in range(1, len(encoded_data) + 1):
        if i == 2**j:
            j += 1
        else:
            decoded_data.append(encoded_data[i - 1])

    return decoded_data

# Ejemplo de uso
data = [1, 0, 1, 1]
encoded_data = hamming_encode(data)
print("Datos codificados:", encoded_data)
decoded_data = hamming_decode(encoded_data)
print("Datos decodificados:", decoded_data)
