numeros = []
j = 7
n, m = 0, 1
for value in range(j):
    numeros.append(n)
    n, m = m, n + m
print (numeros)

fibunnaci_numbers = [0, 1]
for _ in range(0,j-2):
    fib = fibunnaci_numbers[-1]+fibunnaci_numbers[-2]
    fibunnaci_numbers.append(fib)
print(fibunnaci_numbers)

a = 0
b = 1
print(a)
print(b)
for _ in range(0, j-2):
    fib = a+b
    print(fib)
    a = b
    b = fib




