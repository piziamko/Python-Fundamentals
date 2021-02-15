line_1 = input().split()
line_2 = input().split()
line_3 = input().split()
is_no_winner = True

if line_1[1] == line_1[0] == line_1[2] and ("0" not in line_1):
    if line_1[0] == "1":
        print("First player won")
    elif line_1[0] == "2":
        print("Second player won")
    is_no_winner = False
elif line_2[1] == line_2[0] == line_2[2] and ("0" not in line_2):
    if line_2[0] == "1":
        print("First player won")
    elif line_2[0] == "2":
        print("Second player won")
    is_no_winner = False
elif line_3[1] == line_3[0] == line_3[2] and ("0" not in line_3):
    if line_3[0] == "1":
        print("First player won")
    elif line_3[0] == "2":
        print("Second player won")
    is_no_winner = False
elif (line_1[0] == line_2[1] == line_3[2] or line_1[2] == line_2[1] == line_3[0]) and line_2[1] != "0":
    if line_2[1] == "1":
        print("First player won")
    elif line_2[1] == "2":
        print("Second player won")
    is_no_winner = False
else:
    for i in range(len(line_1)):
        if line_1[i] == line_2[i] == line_3[i] and line_1[i] != 0:
            if line_1[i] == "1":
                print("First player won")
            elif line_1[i] == "2":
                print("Second player won")
            is_no_winner = False

if is_no_winner:
    print("Draw!")
