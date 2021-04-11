import os

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

        comidas.append(nombre);
        print("Se ha agregado correctamente.");
    elif opcion == "1":
        nombre = input("Dime un nombre: ");

        if nombre in comidas:
            print(f"La comida {nombre} existe");
        else:
            print(f"La comida no {nombre} existe");
    elif opcion == "2":
        nombre = input("Dime un nombre: ");

        if nombre in comidas:
            comidas.remove(nombre);
            print(f"La comida {nombre} se ha eliminado");
        else:
            print(f"La comida no {nombre} existe");
    elif opcion == "3":
        print("Adios!");
        exit(0);
    else:
        print("La opción no es correcta.");

    os.system("pause");