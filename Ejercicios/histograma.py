
numeros = input("Dime números separados por comas: ");
datos_separados = numeros.split(",");

for numero in datos_separados:
    
    for _ in range(0, int(numero)):
        print("*", end="");
    print();
