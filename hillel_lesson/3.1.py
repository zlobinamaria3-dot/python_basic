number_1=int(input("Enter first number:"))
operator=input("Enter an operator:")
number_2=int(input("Enter second number:"))
match operator:
    case "+":
         number_1+number_2
         print("Result=",number_1+number_2)
    case "-":
         number_1-number_2
         print("Result=",number_1-number_2)
    case "*":
         number_1*number_2
         print("Result=",number_1*number_2)
    case "/":
        match number_2:
            case 0:
                print("Result= error")
            case _:
                number_1/number_2
                print("Result=", number_1/number_2)



