num = int(input())
list_1 = []
list_2 = []
for i in range(num):
    num1 = int(input())
    list_1.append(num1)
key = input()
if key == "even":
    for l in list_1:
        if l % 2 == 0:
            list_2.append(l)
elif key == "odd":
    for l in list_1:
        if l % 2 != 0:
            list_2.append(l)
elif key == "negative":
    for l in list_1:
        if l < 0:
            list_2.append(l)
else:
    for l in list_1:
        if l >= 0:
            list_2.append(l)
print(list_2)
