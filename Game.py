######################## Game ###########################

#def check(i):
#    if type(i) == type(1) and i <= 999:
#        return(i)
#    else:
#        return("or a number of three digits")

def make_an_int_array(st_num):
    ar = []
    for i in st_num:
        ar.append(int(i))
    return(ar)

def clues(user_num, comp_num):
    if user_num == comp_num:
        print("CODE CRACKED!")

    for ind,i in enumerate(user_num):
        if i == comp_num[ind]:
            return("Match")
        elif i in comp_num:
            return("close")
        else:
            return("not even close")



###### generating the random value ######


##### starting the guess ####

def guessing():
    guess = int(input("What is your guess? "))
    #checked = check(guess)
    inputstring = str(guess)
# user's digits
    arr_of_int = make_an_int_array(inputstring)
# calling the clues function
    clues_answer = clues(arr_of_int, shuffled_value)
    print(clues_answer)

    if clues_answer == "Match":
        guessing()


####### Game start ######
import random
digits = list(range(10))
random.shuffle(digits)
# computer's digits
shuffled_value = digits[:3]
print(shuffled_value)

guessing()
