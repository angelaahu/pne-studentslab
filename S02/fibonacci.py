n1 = 0
n2 = 1

for i in range(11):
    if i == 0:
        print(n1, end=" ")
    elif i == 1:
        print(n2, end=" ")
    else:
        a = n1 + n2
        print(a, end= " ")
        n1 = n2
        n2 = a
