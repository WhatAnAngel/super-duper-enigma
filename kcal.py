import re

# Solicitar entradas al usuario
def obtener_peso():
    while True:
        peso_str = input("Ingrese su peso en kg: ")
        if re.match(r'^\d+(,\d+)?$', peso_str):
            peso = float(peso_str.replace(',', '.'))
            return peso
        else:
            print("Entrada inválida. Intente nuevamente.")

peso = obtener_peso()

def obtener_altura():
    while True:
        altura_str = input("Ingrese su altura en cm: ")
        if re.match(r'^\d+(,\d+)?$', altura_str):
            altura = float(altura_str.replace(',', '.'))
            return altura
        else:
            print("Entrada inválida. Intente nuevamente.")

altura = obtener_altura()

def obtener_sexo():
    while True:
        try:
            sexo = int(input("Ingrese su sexo (1: masculino, 2: femenino): "))
            if sexo == 1 or sexo == 2:
                return sexo
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

sexo = obtener_sexo()

def obtener_edad():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            return edad
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

edad = obtener_edad()

def obtener_nivel_actividad():
    while True:
        try:
            print("Niveles de actividad:")
            print("0: Sedentario (poco o ningún ejercicio)")
            print("1: Ligeramente activo (ejercicio ligero o deportes 1-3 días a la semana)")
            print("2: Moderadamente activo (ejercicio moderado o deportes 3-5 días a la semana)")
            print("3: Muy activo (ejercicio intenso o deportes 6-7 días a la semana)")
            print("4: Extremadamente activo (ejercicio muy intenso y trabajo físico diario)")
            nivel_actividad = int(input("Ingrese su nivel de actividad (0-4): "))
            if nivel_actividad >= 0 and nivel_actividad <= 4:
                return nivel_actividad
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

nivel_actividad = obtener_nivel_actividad()

def calcular_imc(peso, altura):
    altura_en_metros = altura / 100
    imc = peso / (altura_en_metros ** 2)
    if imc < 18.5:
        return "Infrapeso"
    elif imc < 25:
        return "Normopeso"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidad tipo I"
    elif imc < 40:
        return "Obesidad tipo II"
    else:
        return "Obesidad tipo III"

IMC = calcular_imc(peso, altura)

def calcular_gasto_energetico(peso, altura, sexo, edad, nivel_actividad, imc):
    if imc.startswith("Obesidad"):
        if sexo == 1:  # Masculino
            gasto_energetico_basal = (10 * peso) + (6.25 * altura) - (5 * edad) + 5
        else:  # Femenino
            gasto_energetico_basal = (10 * peso) + (6.25 * altura) - (5 * edad) - 161
    else:
        if sexo == 1:  # Masculino
            gasto_energetico_basal = 66.5 + (13.75 * peso) + (5.003 * altura) - (6.755 * edad)
        else:  # Femenino
            gasto_energetico_basal = 655.1 + (9.563 * peso) + (1.85 * altura) - (4.676 * edad)

    factores_actividad = [1.2, 1.375, 1.55, 1.725, 1.9]
    factor = factores_actividad[nivel_actividad]
    gasto_energetico_total = gasto_energetico_basal * factor

    return gasto_energetico_basal, gasto_energetico_total

def calcular_calorias(peso, altura, sexo, edad, nivel_actividad):
    imc = calcular_imc(peso, altura)
    gasto_energetico_basal, gasto_energetico_total = calcular_gasto_energetico(peso, altura, sexo, edad, nivel_actividad, imc)

    if imc.startswith("Obesidad"):
        print("Debido a que el IMC indica obesidad, el objetivo se restringe a pérdida de peso.")
        print("Opciones de objetivo:")
        print("1: Pérdida de peso ligera")
        print("2: Pérdida de peso moderada")
        print("3: Pérdida de peso severa")

        while True:
            try:
                objetivo = int(input("Ingrese su objetivo de pérdida de peso (1-3): "))
                if objetivo >= 1 and objetivo <= 3:
                    break
                else:
                    print("Opción inválida. Intente nuevamente.")
            except ValueError:
                print("Entrada inválida. Intente nuevamente.")

        if objetivo == 1:
            calorias = gasto_energetico_total - 300  # Pérdida de peso ligera
        elif objetivo == 2:
            calorias = gasto_energetico_total - 500  # Pérdida de peso moderada
        else:
            calorias = gasto_energetico_total - 700  # Pérdida de peso severa

    else:
        print("Opciones de objetivo:")
        print("1: Pérdida de peso")
        print("2: Mantenimiento de peso")
        print("3: Aumento de peso")

        while True:
            try:
                objetivo = int(input("Ingrese su objetivo: "))
                if objetivo >= 1 and objetivo <= 3:
                    break
                else:
                    print("Opción inválida. Intente nuevamente.")
            except ValueError:
                print("Entrada inválida. Intente nuevamente.")

        if objetivo == 1:
            calorias = gasto_energetico_total - 500
        elif objetivo == 2:
            calorias = gasto_energetico_total
        elif objetivo == 3:
            calorias = gasto_energetico_total + 300
        else:
            calorias = gasto_energetico_total

    calorias = round(calorias, 2)  # Limitar a 2 decimales

    return imc, gasto_energetico_basal, gasto_energetico_total, calorias

# Calcular calorías
IMC, gasto_energetico_basal, gasto_energetico_total, calorias = calcular_calorias(peso, altura, sexo, edad, nivel_actividad)
gasto_energetico_basal = round(gasto_energetico_basal, 2)
gasto_energetico_total = round(gasto_energetico_total, 2)

# Mostrar resultados
print("Estado nutricional (IMC):", IMC)
print("Gasto energético basal:", gasto_energetico_basal, "kcal")
print("Gasto energético total:", gasto_energetico_total, "kcal")
print("Calorías recomendadas:", calorias, "kcal")
