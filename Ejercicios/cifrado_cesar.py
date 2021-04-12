import string

texto_entrada = input("Dime un texto: ").lower();
texto_salida = "";
desplazamiento = 6;

for letra in texto_entrada:
    if letra in string.ascii_lowercase:
        posicion = string.ascii_lowercase.index(letra);
        nueva_posicion = posicion + desplazamiento;

        if nueva_posicion >= len(string.ascii_lowercase):
            nueva_posicion -= len(string.ascii_lowercase);

        texto_salida += string.ascii_lowercase[nueva_posicion];
    else:
        texto_salida += letra;

print(texto_salida);
