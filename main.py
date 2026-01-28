import math
from time import sleep


def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multi(a,b):
    return a*b

def division(a,b):
    return a/b


print("Hello guy, let's keep this simple")
sleep(2)
AnswerDecision= input("Do you want to do:\n1. Sum\n2. Substract\n")

match AnswerDecision:
    case "1":
        print("Great")
        sleep(1)
        a= int(input("Give me the first number: "))
        print("\n\n")
        b= int(input("Give me the second number: "))
        print("\n\n")
        sleep(1)
        print(f"Here is the result of the sum {a} + {b}: {suma(a,b)}")

    case "2":
        print("Great")
        sleep(1)
        a= int(input("Give me the first number: "))
        print("\n\n")
        b= int(input("Give me the second number: "))
        print("\n\n")
        sleep(1)
        print(f"Here is the result of the substraction {a} - {b}: {resta(a,b)}") 

    case "3":
        print("Great")
        sleep(1)
        a= int(input("Give me the first number: "))
        print("\n\n")
        b= int(input("Give me the second number: "))
        print("\n\n")
        sleep(1)
        print(f"Here is the result of the multiplication {a} * {b}: {multi(a,b)}")

    case "4":
        print("Great")
        sleep(1)
        a= int(input("Give me the first number: "))
        print("\n\n")
        b= int(input("Give me the second number: "))
        print("\n\n")
        sleep(1)
        print(f"Here is the result of the division {a} / {b}: {division(a,b)}") 

    case _:
        pass
