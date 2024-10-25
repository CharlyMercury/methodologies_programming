"ENOC"
N = 5
a = 0
b = 1
for i in range(N):
    print(a, end= " ")
    a ,b=b, a+b
print("")
   

if N>2:
    var1, var2, fib, i=0, 1, 0, 1
    print(0,",", 1,",", end=" ")
    while i<=N-2:
        fib=var1+var2
        print(fib, end=", ")
        var1=var2
        var2=fib
        i+=1
   
"""
    Don Charly
"""
print()
print("Don Charly")
# Fib
n = 5
fibunacci = [0, 1]
print(fibunacci[-2], ',', fibunacci[-1], ', ', end='')
for _ in range(0,n-2):
    fib_number = fibunacci[-2]+fibunacci[-1]
    fibunacci.append(fib_number)
    print(fib_number,', ', end='')    
    
    
print()
print()
a = 0
b = 1
print(a)
print(b)
for _ in range(0, n-2):
    fib = a +b 
    print(fib)
    a = b 
    b = fib