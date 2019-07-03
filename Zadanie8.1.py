# 8.1 W Stringu mogą się znaleźć również bomby - znaki '*',
# które wymazują przyległe litery, na przykład:
# aa*aa => a__a
# aa => ____

# Przykład stringów:
# zzzz*s*
# www*www****z
# *zd*qm*wp*bs*

contest_string = input("Please type in the contest string: ")
contest_list = list(contest_string)

def letterbattle(contest_list):

    if "*" in contest_list:
        position = contest_list.index("*")
        if position > len(contest_list):
            del contest_list[position - 1]
            del contest_list[position + 1]
        else:
            del contest_list[position - 1]

    left_score = 0
    right_score = 0
    for i in contest_list:
        if i == "w":
            left_score += 4
        if i == "p":
            left_score += 3
        if i == "b":
            left_score += 2
        if i == "s":
            left_score += 1
        if i == "m":
            right_score += 4
        if i == "q":
            right_score += 3
        if i == "d":
            right_score += 2
        if i == "z":
            right_score += 1

    if left_score == right_score:
        print(" It's a draw! ")
    elif left_score > right_score:
        print(" Left side won! ")
    else:
        print(" Right side won!")

letterbattle(contest_list)