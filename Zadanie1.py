# 5.  Napisz program, który wczytuje ze standardowego wejścia nieujemną liczbę całkowitą n
# i wypisuje na standardowym wyjściu sumę kwadratów liczb od 0 do n, czyli wartość 0^2 + 1^2 + 3^2 + ... + n^2.

n = int(input("Type in the number: "))
count = 0
squares = []
while count <= n:
    squares.append(count **2)
    count = count + 1
print(sum(squares))
