import random

numero_aleatorio = random.randint(1, 20);
numero_jugador = int(input("Dime un número: "));

if numero_aleatorio == numero_jugador:
    print("¡Has acertado!");
else:
    print(f"¡Has fallado! El número era {numero_aleatorio}");
