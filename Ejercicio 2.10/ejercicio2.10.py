def metrosApulgadas(metros):
    '''Convertir metros a pulgadas usando el factor de conversión 1 pulgada = 0.0254 metros.'''
    pulgadas = metros / 0.0254  # Dividir por 0.0254 para convertir metros a pulgadas
    return pulgadas


# Ingresar la cantidad de metros
metros = float(input("Ingrese la cantidad de tela en metros: "))

# Realizar la conversión
pulgadas = metrosApulgadas(metros)

# Redondear el resultado a dos decimales
pulgadasRedondeadas = round(pulgadas, 2)

# Mostrar el resultado de la conversión
print(f"{metros} metros equivalen a {pulgadasRedondeadas} pulgadas")

# Fin del programa
print("Conversión completada.")
        