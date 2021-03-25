first_num = float(input("Enter the first number : "))
op = input("Enter the operator : ")
second_num = float(input("Enter the second number : "))



if op == '+' :
    print( first_num + second_num )
elif op == '-' :
    print( first_num - second_num )
elif op == '*' :
    print( first_num * second_num )
elif op == '/' :
    print( first_num / second_num )
elif op == '//' :
    print( first_num // second_num )
elif op == '%' :
    print( first_num % second_num )
elif op == '^' :
    print( first_num ** second_num )
else :
    print("you didn't enter a correct operator ! ")
