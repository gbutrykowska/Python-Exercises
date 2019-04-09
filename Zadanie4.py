#4. Napisz program, który wczytuje ze standardowego wejścia nieujemną liczbę całkowitą n
#i wypisuje na standardowym wyjściu element ciągu Fibonacciego o indeksie n.

n = int(input("Type in the number: "))
numbers = list(range(0,n))
x, y = 0, 1

for number in numbers:
	x, y = y, x+y
print(x)
