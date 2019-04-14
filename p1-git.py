def sumatodos(limitado):
    resultado=0
    for i in range(0,limitado+1):
        resultado +=i
        
    return resultado
def sumacuadrados(limitado):
    resultado=0
    for i in range(0,limitado+1):
        resultado += i*i
    return resultado

print("hola",sumatodos(100))
print (sumacuadrados(3))