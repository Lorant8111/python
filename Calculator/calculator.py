relaciosjel = input("Írj be egy relációs jelet (+ - * /): ")
num1 = float(input("Írd be az 1. számod: "))
num2 = float(input("Írd be a 2. számod: "))

if relaciosjel == "+":
    result = num1 + num2
    print(round(result, 3))
elif relaciosjel == "-":
    result = num1 - num2
    print(round(result, 3))
elif relaciosjel == "*":
    result = num1 * num2
    print(round(result, 3))
elif relaciosjel == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{relaciosjel} ez nem egy valós relációs jel")