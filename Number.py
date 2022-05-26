inicio = True
while inicio == True:
    valor1 = int(input("     Ingresar valor):"))
    valor2 = int(input("     Ingresar otro valor):"))

    print("     ¿Que desea hacer con? >>",valor1," y ",valor2)
    print("     s para Sumar        r para Restar       m para Multiplicar      d para Dividir      off para Apagar")
    opcion = input("        >> ")

    if opcion == "s":
        def Sum():
            var = valor1 + valor2
            return var
        print("     ",valor1," + ",valor2," = ",Sum())

    elif opcion == "m":
        def Mult():
            var = valor1 * valor2
            return var
        print("     ",valor1," . ",valor2," = ",Mult())

    elif opcion == "r":
        def Res():
            var = valor1 - valor2
            return var
        print("     ",valor1," - ",valor2," = ",Res())

    elif opcion == "d":
        def Div():
            var = valor1 // valor2
            return var
        print("     ",valor1," : ",valor2," = ",Div())
    
    elif opcion == "off":
        inicio = False