
def calculadora (num1, num2):
    suma= num1+num2
    resta=num1-num2
    mul=num1*num2
    div=num1/num2
    return suma, resta, mul, div

calcu = calculadora (5,5)
print(calcu)