#4. Napisz program, który wczytuje ze standardowego wejścia nieujemną liczbę całkowitą n
#i wypisuje na standardowym wyjściu element ciągu Fibonacciego o indeksie n.

n = int(input("Type in the number: "))
count = 1
x, y = 0, 1
while count <= n:
    x, y = y, x + y
    count = count + 1
print(x)