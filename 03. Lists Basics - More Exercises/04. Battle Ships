n = int(input())

field = {}
for i in range(n):
    field[i] = [int(k) for k in input().split()]

attacked = [j for j in input().split()]
attack_dict = {}
for i in range(1, len(attacked) + 1):
    attack_dict[i] = [int(k) for k in attacked[i - 1].split("-")]

count_ship = 0

for i in attack_dict:
    row = attack_dict[i][0]
    col = attack_dict[i][1]
    if field[row][col] != 0:
        field[row][col] -= 1
        if field[row][col] == 0:
            count_ship += 1

print(count_ship)
