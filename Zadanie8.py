#8. Istnieją dwie grupy walczących liter. Napisz program, który wczytuje String rozgrywki
# składający się z liter oraz decyduje, która grupa zwyciężyła turę.
#Lewa strona:
#w - 4
#p - 3
#b - 2
#s - 1
#Prawa strona:
#m - 4
#q - 3
#d - 2
#z - 1
#Pozostałe litery nie mają znaczenia w rozgrywce.
#Przykład: "zdqmwpbs"
#Przydatna będzie metoda: String.toCharArray

def get_left_score(contest_list):
    left_score = 0
    for letter in contest_list:
        if letter == "w":
            left_score += 4
        if letter == "p":
            left_score += 3
        if letter == "b":
            left_score += 2
        if letter == "s":
            left_score += 1
    return left_score

def get_right_score(contest_list):
    right_score = 0
    for letter in contest_list:
        if letter == "m":
            right_score += 4
        if letter == "q":
            right_score += 3
        if letter == "d":
            right_score += 2
        if letter == "z":
            right_score += 1
    return right_score

def print_letter_battle_result(left_score, right_score):
    if left_score == right_score:
        print(" It's a draw! ")
    elif left_score > right_score:
        print(" Left side won! ")
    else:
        print(" Right side won!")




contest_string = input("Please type in the contest string: ")
contest_list = list(contest_string)

left_score = get_left_score(contest_list)
right_score = get_right_score(contest_list)
print_letter_battle_result(left_score, right_score)
