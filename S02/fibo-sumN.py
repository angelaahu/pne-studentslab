def fibon(n):
    n1 = 0
    n2 = 1

    if n == 0:
        result = n1
    elif n == 1:
        result = n2
    else:
        for i in range(2, n+1):
            a = n1 + n2
            n1 = n2
            n2 = a
        result = n2

    return result

def fibosum(n):
    total = 0
    for i in range(1, n + 1):
        total = total + fibon(i)
    return total

print("Sum of the first 5 terms of the Fibonacci series: ", fibosum(5))
print("Sum of the first 10 terms of the Fibonacci series: ", fibosum(10))