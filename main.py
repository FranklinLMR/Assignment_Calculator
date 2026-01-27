import math
from time import sleep

print("Hello guy, let's keep this simple")
sleep(2)
AnswerDecision= input("Do you want to do:\n1. Sum\n2. Substract")
match AnswerDecision:
    case "1":
        print("Great")
        sleep(1)
        n1= int(input("Give me the first number: "))
        print("\n\n")
        n2= int(input("Give me the second number: "))

        print(f"Here is the result of the sum: {n1+n2}")

    case "2":
        print("Great")
        sleep(1)
        n1= int(input("Give me the first number: "))
        print("\n\n")
        n2= int(input("Give me the second number: "))

        print(f"Here is the result of the substraction: {n1-n2}") 

    case _:
        pass