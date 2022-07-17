num = (1,2,3,4,5,6,7,8,9)
lst_even = []
lst_odd = []
for i in num:
    if i % 2 == 0:
        lst_even.append(i)
    else:
        lst_odd.append(i)
print(lst_even, lst_odd)