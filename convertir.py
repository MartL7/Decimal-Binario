#Codigo que convierte de Decimal a Binario

#Codigo By: Geovas or MartL7

#Variable para hacer un bucle el programa se reiniciara cuando el usuario decida
Reinicio = True

while Reinicio:
    #Codigo que convierte de Decimal a Binario
    def ConvertirBinario(numero):
        if numero == 0:
            return '0'
        
        binario = ''
        while numero > 0:
            binario = str(numero % 2) + binario
            numero = numero // 2
        return binario

    numero = int(input("Ingresa un numero decimal: "))
    NumeroBinario = ConvertirBinario(numero)

    print("El numero binario de ", numero, " es: ",NumeroBinario)

    OtraVez = input("¿Deseas convertir otro nÚmero? (Si/No): ").lower()
    if OtraVez != "si":
        print("Chao 😂")
        break;