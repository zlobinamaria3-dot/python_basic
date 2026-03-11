# 3.2
first_list = [12, 3, 4, 10]
new_list=[first_list[-1]] + first_list[:-1]
print(new_list)

second_list = [12, 3, 4, 10, 8]
new_list=[second_list[-1]] + second_list[:-1]
print(new_list)
# 3.3
my_list=[]
middle_index = len(my_list) // 2
if len(my_list) % 2 != 0 :
    middle_index += 1
    first_list=my_list[:middle_index]
    print(first_list)
    second_list=my_list[middle_index:]
    print(second_list)
    result = ([first_list] + [second_list])
    print(result)
if len(my_list) % 2 == 0:
    first_list=my_list[:middle_index]
    print(first_list)
    second_list=my_list[middle_index:]
    print(second_list)
    result = ([first_list] + [second_list])
    print(result)








