import datetime

dia = int(input("Dime un dia: "));
mes = int(input("Dime un mes: "));
anno = int(input("Dime un año: "));

dias_vividos1 = (2021 - anno) * 365;
print(f"Has vivido {dias_vividos1} días, y de ellos has dormido {int(dias_vividos1 / 3)}");


ahora = datetime.datetime.today();
fecha_nacimiento = datetime.datetime.strptime(f"{dia}/{mes}/{anno}", "%d/%m/%Y");

resultado = ahora - fecha_nacimiento;
print(f"Has vivido {resultado.days} días, y de ellos has dormido {int(resultado.days / 3)}");
