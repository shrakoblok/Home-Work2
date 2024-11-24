import random

first_paste = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
first_number = random.choice(first_paste)
result = []
for i in range(1, first_number + 1):
    for j in range(1, first_number):
        if i == j:
            continue
        if first_number % (i + j) == 0:
            if (str(j) + '.' + str(i)) in result:
                continue
            result.append(str(i) + '.' + str(j))
print(''.join(result).replace('.', ''))
