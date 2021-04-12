import string

def normalizar_texto(texto):
    acentos = { "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u" };
    for letra_acentuada, nueva_letra in acentos.items():
        texto = texto.replace(letra_acentuada, nueva_letra);

    for simbolo in string.punctuation:
        texto = texto.replace(simbolo, "");

    texto = texto.replace(" ", "");

    return texto;

def comprobrar_si_palindromo(texto):
    es_palindromo = True;
    posicion = 0;

    while es_palindromo and posicion < int(len(texto_entrada) / 2):

        if texto_entrada[posicion] != texto_entrada[-(posicion + 1)]:
            es_palindromo = False;

        posicion += 1;

    return es_palindromo;

texto_entrada = input("Dime un texto: ").lower();
texto_entrada = normalizar_texto(texto_entrada);

print(comprobrar_si_palindromo(texto_entrada));
