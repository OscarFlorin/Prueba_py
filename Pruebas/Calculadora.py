#Este es mi segunda prueba para github, este programa hace las operaciones simples de dos numeros que ingrese el usuario.

def calculadora_operaciones_basicas(num1, num2):
    print(f"La suma de {num1} + {num2} = {num1+num2}")
    print(f"La resta de {num1} - {num2} = {num1-num2}")
    print(f"La multiplicación de {num1} x {num2} = {num1*num2}")
    print(f"La división de {num1} / {num2} = {num1/num2}")
    print(f"La division entera de {num1} // {num2} = {num1//num2}")
    print(f"La exponente {num1} ** {num2} = {num1**num2}")    
    print(f"La residuo de {num1} % {num2} = {num1%num2}")


    print(f"\n*************************************")
    print(f"\nTabla de multiplicar del numero {num1}")
    for numero in range(1,11):
        print(f"{num1} x {numero} = {num1 * numero}")
    else:
        print("Tabla finalizada!!")


    print(f"\n*************************************")
    print(f"\nTabla de multiplicar del numero {num2}")
    for numero in range(1,11):
        print(f"{num2} x {numero} = {num2 * numero}")
    else:
        print("Tabla finalizada!!")
    

num1 =int(input("Ingresa el primer numero positivo: "))
num2 =int(input("Ingresa el segundo numero positivo: "))
calculadora_operaciones_basicas(num1,num2)

