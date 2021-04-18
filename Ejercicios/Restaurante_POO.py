import os

class Comida():
    def __init__(self, nombre, precio, peso):
        self.nombre = nombre;
        self.precio = precio;
        self.peso = peso;

comidas = [];

while True:
    os.system("cls");

    print("Restaurante - Gestión");
    print("[0] Agregar comida");
    print("[1] Consultar comida");
    print("[2] Eliminar comida");
    print("[3] Salir");

    opcion = input("Dime una opcion: ");

    if opcion == "0":
        nombre = input("Dime una comida: ");
        precio = float(input("Dime un precio: "));
        peso = float(input("Dime un peso: "));

        nueva_comida = Comida(nombre, precio, peso);

        comidas.append(nueva_comida);
        print("Se ha agregado correctamente.");
    elif opcion == "1":
        nombre = input("Dime un nombre: ");

        for comida in comidas:
            if comida.nombre == nombre:
                print(f"La comida {nombre} existe");

    elif opcion == "2":
        nombre = input("Dime un nombre: ");

        for comida in comidas:
            if comida.nombre == nombre:
                comidas.remove(comida);
                print(f"La comida {nombre} se ha eliminado");

    elif opcion == "3":
        print("Adios!");
        exit(0);
    else:
        print("La opción no es correcta.");

    os.system("pause");