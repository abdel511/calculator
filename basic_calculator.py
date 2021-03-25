first_num = float(input("Enter the first number : "))
op = input("Enter the operator : ")
second_num = float(input("Enter the second number : "))

def factorial(num):
    fact = 1
    if num < 0:
        print("can't calculate the factorial of a negative number!")
    elif num == 0 :
        print(1)
    else:
        for i in range(1,int(num)+1):
            fact *= i
        print(fact)


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
elif op == '!' :
    print( factorial(first_num) )
else :
    print("you didn't enter a correct operator ! ")
