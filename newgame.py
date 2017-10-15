# 1. The computer will think of 3 digit number that has no repeating digits.
import random

def generat_num():
    digits = list(range(10))
    random.shuffle(digits)
    shuf_num = digits[:3]
    arr1 = [str(digits[1]), str(digits[2]), str(digits[3])]
    return(arr1)


# 2. You will then guess a 3 digit number
def guessing():
    guess = input("What is your guess? ")
    arr2 = [guess[0], guess[1], guess[2]]
    return(arr2)


# 3. The possible clues are:
def cluesg(user, com):
    finish = ""
    if user == com:
        finish = "CODE CRACKED!"
        print(finish)
    else:
        arr3 = []
        for ind,i in enumerate(user):
            if i == com[ind]:
                arr3.append("match")
            elif i in com:
                arr3.append("close")
            else:
                arr3.append("not even close")
            print (arr3)
    if finish != "CODE CRACKED!":
        first_function_call(guessing(), com)
    else:
        print("Good Game")

def first_function_call(a, b):
    cluesg(a, b)

cmp_code = generat_num()
print(cmp_code)
user_code = guessing()
print(user_code)
first_function_call(user_code, cmp_code)
