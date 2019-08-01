# 7. Dana jest wejściowa tablica integerów. Należy znaleźć czy istnieją pary liczb stojące przy sobie,
# sumujące się do podanej sumy (t). Jeśli tak, należy usunąć drugą liczbę z pary z tablicy
# i zwrócić tablicę wynikową.
# Przykład:

# x = [1, 2, 3, 4, 5]
# y = [1, 2, 2, 3, 4, 5]
# t = 3

# 1+2 = t, więc wyrzucamy 2. Żadna inna para nie sumuje się do t, więć wynikiem jest:
# [1, 3, 4, 5]

def check_if_sums_to(int_list, t):
        for n in range(0, len(int_list)-2):
            if int_list[n] + int_list[n + 1] == t:
                del int_list[n + 1]
        return int_list

input_string = input("Input integers separated by space: ")
list = list(input_string.split())
int_list = [int(i) for i in list]
t = int(input("Input the sum: "))

check_if_sums_to(int_list, t)
print(int_list)
