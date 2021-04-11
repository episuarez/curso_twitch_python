import string

letra = input("Dime una letra: ");

letra = letra.lower();

letra = letra.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u");

if len(letra) != 1:
    print("Error en datos: Más de una letra");
elif letra.isdigit():
    print("Error en datos: No se aceptas números");
elif not letra in string.ascii_lowercase:
    print("Error en datos: No se acepta caracter alfanumerico");
else:
    if letra in "aeoiu":
        print("Es una vocal");
    else:
        print("Es una consonante");