import string

def generar_cifrado_cesar(texto):
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

    return texto_salida;

texto_entrada = input("Dime un texto: ").lower();
print(generar_cifrado_cesar(texto_entrada));
