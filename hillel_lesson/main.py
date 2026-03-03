
#1
number=5**2
print(number)
#2
number = int(input("Please enter three numbers: "))
n1 = number // 100
n2 = number % 100 // 10
n3 = number % 10
print((n1+n2+n3)/3)
#3
#version1
number = int(input("Please enter minutes: "))
n1 = number // 100
n2 = number % 100 // 10
n3 = number % 10
result1=number//60
result2=(number%60)
print(f"{result1} hours {result2} minutes")
#version2
number = int(input("Please enter minutes: "))
converter=(divmod(number, 60))
print(converter[0], "hours", converter[1], "minutes")
#4
price = int(input("Enter price:"))
discount= int(input("Enter discount(%):"))
print(price-((price*discount)/100))
#5
#version1 for any number
number = input("Please enter the number: ")
print(number[-1])
#version2
number = int(input("Please enter the number: "))
last_n = number % 10
print(last_n)
#6
rectangle_a = int(input("Please enter length: "))
rectangle_b = int(input("Please enter width: "))
perimeter = ((rectangle_a + rectangle_b)*2)
print("Perimeter: ", perimeter)
#7
#version1
number = input("Please enter 4-digit number: ")
print(number[0])
print(number[1])
print(number[2])
print(number[3])
#version2
number = int(input("Please enter 4-digit number: "))
n1 = number // 1000
n2 = number % 1000 // 100
n3 = number % 100 // 10
n4 = number % 10
print(n1)
print(n2)
print(n3)
print(n4)













