
num1 = 0
num2 = 1
print(num1)
print(num2)
for _ in range(2,11):
    num3 = num1 + num2
    print(num3)
    num1 = num2
    num2 = num3


"""
    Charly
"""
print("Programa de Don Charly Mercury")
fibunacci = [0, 1]
n = 5
for _ in range(0,n-2):
    fibunacci.append(fibunacci[-1]+fibunacci[-2])
print(fibunacci)





fibonacci = [0,1]
n=5
for _ in range(0,n-2):
    fibonacci.append(sum(fibonacci[-2:]))
print(fibonacci)    