def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Ingrese el valor de n para calcular el n-ésimo número de Fibonacci: "))

if n < 0:
    print("El número de Fibonacci no está definido para valores negativos.")
else:
    result = fibonacci(n)
    print(f"El {n}-ésimo número de Fibonacci es {result}")