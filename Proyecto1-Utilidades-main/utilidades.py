EURO_BITCOIN_RATE = 44471.78
ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚ"


def sumar_numeros(num1, num2):
    '''Suma los dos numeros proporcionados.'''
    suma = num1 + num2
    return suma

# 1. Conversor de criptomonedas


def euros_a_bitcoins(euros: int | float):
    '''Convierte una cantidad de euros a bitcoins. 1 bitcoin = 44570.17 €'''
    return round(euros/EURO_BITCOIN_RATE, 2)


def bitcoins_a_euros(euros: int | float) -> int | float:
    '''Convierte una cantidad de bitcoins a euros. 1 bitcoin = 44570.17 €'''
    return round(EURO_BITCOIN_RATE*euros, 2)


# 2. Contador de vocales
def contar_vocales(texto: str) -> int:
    '''Devuelve el número de vocales que tiene el texto dado.'''
    total_vocales = 0

    for l in texto.lower():
        if l in ("a", "e", "i", "o", "u"):
            total_vocales += 1

    return total_vocales


# 3. Detector de palíndromos
def es_palindromo(texto: str) -> bool:
    '''Detecta si un texto es palíndromo o no'''
    texto = texto.lower().replace(" ", "")
    texto_reves = texto[::-1]

    return texto == texto_reves


# 4. Detector de máximos de temperaturas
def max_temperaturas(temperaturas: list[float], umbral: float) -> list[float]:
    '''Detecta qué mediciones de temperatura han superado el umbral dado'''
    temps_validas = []

    for t in temperaturas:
        if t > umbral:
            temps_validas.append(t)

    return temps_validas


# 5. Lista de la compra
productos: list[str] = []


def insertar(producto: str) -> None:
    '''Añade un producto a la lista'''
    productos.append(producto)


def borrar(numero: int) -> None:
    '''Borra el producto en el índice dado de lista de productos.'''
    productos.pop(numero)


def mostrar_productos() -> None:
    '''Muestra la lista de productos con sus índices.'''
    if len(productos) == 0:
        print("No hay productos")

    else:
        i = 0
        for p in productos:
            print(f"{i}: {p}")
            i += 1


def cantidad() -> int:
    '''Devuelve el número de productos.'''
    return len(productos)


# 6. Cifrado de texto (opcional)
def cifrar(texto: str, desplazamiento: int) -> str:
    '''
    Transforma un texto dado usando cifrado César con un desplazamiento dado.

    Utiliza esta lista de caracteres: ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚ

    Si un caracter no se encuentra en la lista, se deja intacto.
    '''

    texto = texto.upper()
    texto_cifrado = ""

    for l in texto:
        indice = ALFABETO.find(l)
        if indice == -1:
            texto_cifrado += l

        else:
            indice = (indice + desplazamiento) % len(ALFABETO)
            texto_cifrado += ALFABETO[indice]

    return texto_cifrado


def descifrar(cifrado: str, desplazamiento: int) -> str:
    '''
    Aplicada a un texto cifrado con el mismo desplazamiento,
    devuelve el texto original.
    '''

    cifrado = cifrado.upper()
    texto_cifrado = ""

    for l in cifrado:
        indice = ALFABETO.find(l)
        if indice == -1:
            texto_cifrado += l

        else:
            indice = (indice - desplazamiento) % len(ALFABETO)
            texto_cifrado += ALFABETO[indice]

    return texto_cifrado

# def descifrar(cifrado: str, desplazamiento: int) -> str:
#   '''
# #   Aplicada a un texto cifrado con el mismo desplazamiento,
#   devuelve el texto original.
#   '''

#   cifrar(cifrado, -desplazamiento)


# 7. Menú de selección
def menuInteractivo() -> None:

    print("Menú interactivo \n")
    while True:
        accion = input("-> ").lower()

        match(accion.split()):
            case["convertir", "euros", "bitcoins", valor]:
                print(euros_a_bitcoins(float(valor)))
                print("\n")

            case["convertir", "bitcoins", "euros", valor]:
                print(bitcoins_a_euros(float(valor)))
                print("\n")

            case["contar", *texto]:
                print(contar_vocales(" ".join(texto)))
                print("\n")

            case["palindromo", texto]:
                print(es_palindromo(texto))
                print("\n")

            case["temperaturas", temps, umbral]:
                temps_a_float = []
                for t in temps.split(","):
                    temps_a_float.append(float(t))

                print(max_temperaturas(temps_a_float, float(umbral)))
                print("\n")

            case["cifrar", texto, desplazamiento]:
                print(cifrar(texto, int(desplazamiento)))
                print("\n")

            case["descifrar", texto, desplazamiento]:
                print(descifrar(texto, int(desplazamiento)))
                print("\n")

            case["productos"]:
                mostrar_productos()
                print("\n")

            case["productos", "nuevo", pdto]:
                insertar(pdto)
                print("\n")

            case["productos", "borrar", pdto]:
                borrar(int(pdto))
                print("\n")

            case["salir"]:
                print("¡Adiós!")
                print("\n")
                break

            case _:
                print("Comando no reconocido \n")


# Bloque de ejecución
if __name__ == '__main__':
    menuInteractivo()
