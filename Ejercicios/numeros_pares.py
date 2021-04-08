
numero1 = int(input("Dime un numero: "));
numero2 = int(input("Dime un numero: "));

contador = 0;

paso = 1;
if numero1 > numero2:
    paso = -1;

for numero in range(numero1, numero2 + paso, paso):
    if numero % 2 == 0:
        contador += 1;

print(f"Hay {contador} numero pares");
