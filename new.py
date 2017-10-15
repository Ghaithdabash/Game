from random import shuffle


my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
#print(my_taxes)
############Strings#############
mystring = "abcdefg"
#print (mystring)
#print (mystring[-1])
#print (mystring[2])
#print (mystring[:2])
#print (mystring[2:])
#print (mystring[2:5])# from index 2 to index 5
#print (mystring[::2])# skipping two digits every time

u = mystring.upper()
#print (u)
l = mystring.lower()
#print (l)

c = mystring.capitalize()
#print(c)
########### Print formatting ##########

p = "Insert something:{}" .format("sluck")
#print(p)

######### list ##########
mylist = [1,2,3]
#or
#mylst = ['so','what the fuck',5,888,'aef',[1,5,9]]
#print(len(mylist))#length

newlist = ['a','b','c']
#print (newlist)
newlist.append("new item")#adding one value to the list
newlist.extend(['r','j','e'])#extending the list
#print(newlist)

item = newlist.pop(3)
#print(item)
#print(newlist)
# we can  use sort() and reverse() on the list
# nested lists can be manipulated easely by print (listname[][])

matrix = [[1,2,3],[4,5,6],[7,8,9]]
#list comprehension
first_col = [row[0] for row in matrix]
second_col = [row[1] for row in matrix]
third_col = [row[2] for row in matrix]

#print(first_col, second_col, third_col)

############# Hash table (dictionaries) (objects) #############

my_stuff = {'lunch':'pizza', 'bfast':'eggs'}
my_stuff ['lunch'] = 'burger'
my_stuff ['dinner'] = 'pasta'
#print(my_stuff)

############# Tuples ##############

############ sets ############
# it is only used for unique values (without repeating values)
x = set()

x.add(1)
x.add(2)
x.add(0.2)

#print(x)

#(ages = {"Sam":3,"Frank":4,"Dan":29}
#i=1
#for key in ages:
#    print(i,':')
#    print("This is the key :",key)
#    print("This is the value :", ages[key])
#    i+=1

x = [1,2,3,4]


i = 0
for item in x:
    x[i]=item**2
    i+=1

#print(x)

#print([item**2 for item in x])


def my_fun(param1='zeft'):
    """
    any fuck
    """
#    print('my first', param1)

my_fun()




def hello():
    return"hello"



def stringBits(v):
    s=""
    for i in range(len(v)):
        if i%2==0:
            s=s+v[i]
    print(s)


d="5ara"
#stringBits(d)

def end_other(a, b):
    a = a.upper()
    b = b.upper()
    if a.endswith(b) or b.endswith(a):
        print(True)
    else:
        print(False)

#end_other("asD","hdhthasd")


def arrayCheck(nums):
    if 1 in nums and 2 in nums and 3 in nums:
        print(True)
    else:
        print(False)


a = [1, 1, 2, 4, 1]
#arrayCheck(a)



def doubleChar(st):
    s = ""
    for lo in st:
        s += lo + lo
    print(s)

ss = "the"
#doubleChar(ss)
#################################
class Book():
    def __init__(self, title, author, pages):
        print ("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title:%s , author:%s, pages:%s " %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print ("A book is destroyed")

#book = Book("Python Rocks!", "Jose Portilla", 159)

#Special Methods
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
allcards = [(s,r) for s in SUITE for r in RANKS ]
print(allcards)
