a=float(input("enter num1:"))
b=float(input("enter num2:"))
choice=input("enter choice=")
match choice:
    case '+':
        print("sum:",a+b)
    case '-':
        print("difference:",a-b)
    case '*':
        print("mul:",a*b)
    case '%':
        print("mod:",a%b)
    case '//':
        print("floor:",a//b)
    case _:
        print("invalid")
