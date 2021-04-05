
nombre = input("Dime un nombre: ");
edad = input("Dime una edad: ");

print("Hola " + nombre + ", tienes " + edad + " años");
print("Hola ", nombre, ", tienes ", edad, " años", sep="");

print(f"Hola {nombre}, tienes {edad} años"); # A partir 3.6
