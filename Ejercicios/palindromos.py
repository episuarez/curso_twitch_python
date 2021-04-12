import string

texto_entrada = input("Dime un texto: ").lower();
es_palindromo = True;
posicion = 0;

acentos = { "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u" };
for letra_acentuada, nueva_letra in acentos.items():
    texto_entrada = texto_entrada.replace(letra_acentuada, nueva_letra);

for simbolo in string.punctuation:
    texto_entrada = texto_entrada.replace(simbolo, "");

texto_entrada = texto_entrada.replace(" ", "");

while es_palindromo and posicion < int(len(texto_entrada) / 2):

    if texto_entrada[posicion] != texto_entrada[-(posicion + 1)]:
        es_palindromo = False;

    posicion += 1;

print(es_palindromo);
