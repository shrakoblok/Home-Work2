my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
ind = 0
while ind < len(my_list):
    if my_list[ind] >= 0:
        if my_list[ind] == 0:
            ind += 1
            continue
        print(my_list[ind])
        ind += 1
    else:
        break
