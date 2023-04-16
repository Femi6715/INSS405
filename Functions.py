def request():
    num1=input('Enter varaiable num1')
    num2 = input('Enter varaiable num2')
    print(addition(num1,num2))
    print(subtraction(num1,num2))
    print(multiplication(num1,num2))
    print(division(num1,num2))



def addition(num1,num2):
    sum=int(num1)+int(num2)
    return sum


def subtraction(num1,num2):
    difference=int(num1)-int(num2)
    return difference

def multiplication(num1,num2):
    mult=int(num1)*int(num2)
    return mult


def division(num1,num2):
    div=int(num1)/int(num2)
    return div


request()