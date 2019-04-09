#3. Napisz program, który wczytuje ze standardowego wejścia trzy liczby całkowite
#i wypisuje na standardowym wyjściu największą z ich wartości
#(pamiętaj o przypadku gdy wszystkie podane liczby lub dwie z nich są równe).

x = int(input("Type in first integer:"))
y = int(input("Type in second integer:"))
z = int(input("Type in third integer:"))
if (x>=y) and (x>=z):
    print(x)
elif (y>=x) and (y>=z):
    print(y)
else:
    print(z)