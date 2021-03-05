sequence = input().split()
command = input()

while not command == "end":
    command = command.split()
    type_com = command[0]
    if type_com == "reverse":
        start = int(command[2])
        count = int(command[4])
        sequence[start:(start+count)] = sequence[(start+count-1):start-1:-1]
    elif type_com == "sort":
        start = int(command[2])
        count = int(command[4])
        sequence[start:(start+count)] = sorted(sequence[start:(start+count)])
    elif type_com == "remove":
        count = int(command[1])
        del sequence[:count]

    command = input()
sequence = list(map(str, sequence))
print(*sequence, sep=", ")
