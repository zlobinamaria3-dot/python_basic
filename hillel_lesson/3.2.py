# 3.2
first_list = [12, 3, 4, 10]
new_list=[first_list[-1]] + first_list[:-1]
print(new_list)

second_list = [12, 3, 4, 10, 8]
new_list=[second_list[-1]] + second_list[:-1]
print(new_list)