# 5. Napisz program, który wczytuje ze standardowego wejścia nieujemną liczbę całkowitą n
# i wypisuje na standardowym wyjściu sumę kwadratów liczb od 0 do n, czyli wartość 0^2 + 1^2 + 3^2 + ... + n^2.

n = int(input("Type in the number: "))
numbers = list(range(0,n+1))
squares = []

for number in numbers:
	squares.append(number**2)

print(sum(squares))