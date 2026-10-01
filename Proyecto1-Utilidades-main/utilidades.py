EURO_BITCOIN_RATE = 44471.78

def sumar_numeros(num1, num2):
    '''Suma los dos numeros proporcionados.'''
    suma = num1 + num2
    return suma

def euros_a_bitcoins(euros: int | float):
  '''Convierte una cantidad de euros a bitcoins. 1 bitcoin = 44570.17 €'''
  return euros/EURO_BITCOIN_RATE

def bitcoins_a_euros(euros: int | float) -> int | float:
  '''Convierte una cantidad de bitcoins a euros. 1 bitcoin = 44570.17 €'''
  return EURO_BITCOIN_RATE*euros 

def contar_vocales(texto: str):
  '''Devuelve el número de vocales que tiene el texto dado.'''
  total_vocales = 0
  
  for l in texto.lower():
    if l in ("a","e","i","o","u"):
      total_vocales += 1
   
  return total_vocales

def es_palindromo(texto: str):
  '''Detecta si un texto es palíndromo o no'''
  raise NotImplementedError