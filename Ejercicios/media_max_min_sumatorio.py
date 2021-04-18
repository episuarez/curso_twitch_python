
numeros = [];

for _ in range(0, 10):
    numeros.append(int(input("Dime un número: ")));

def sumatorio():
    total = 0;

    for numero in numeros:
        total += numero;

    return total;

def media():
    return sumatorio() / len(numeros);

def maximo():
    maximo = numeros[0];

    for numero in numeros:
        if numero > maximo:
            maximo = numero;

    return maximo;

def minimo():
    datos = sorted(numeros);

    return datos[0];

print(sumatorio());
print(media());
print(maximo());
print(minimo());