#using comprehension
number_list = [num for num in range(1, 101)]
even_list = [num for num in range(1, 101) if num % 2 == 0]
print(number_list)
print(even_list)

list100 = list(range(1, 100))
print(list100)

even_list =[]
for num in range(1,101):
    if num % 2 == 0:
        even_list.append(num)
print(even_list)


set_compr = {item for item in range(1, 101)}
print(set_compr)




ascii_dict = {key: ord(str(key)) for key in range(1, 10)}  # ord stands for ordenance and execute for ascii number
print(ascii_dict)