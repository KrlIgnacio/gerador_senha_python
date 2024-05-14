import string as str
import numpy as np

# alfabeto
letras = str.ascii_letters
# numeros - 0 à 9
numeros = str.digits
# caracteres especiais 
caracter = str.punctuation

# a senha deve concatenar -> letras, numeros, caracteres
algarismos = letras + numeros + caracter

# gerando senha aleatória com 10 algarismos
senha = np.random.choice(list(algarismos), 10)

print(''.join(senha))