#variable are container for a value
vari = "this is string"
#variable can be combain as long as it is of same data type
print(type(vari))
#it will print data type of variable "vari"
#age += 1 ---> age = age + 1
#print(string + integer) will not work as these two are of different data type and for its solution will be to use type casting ---> print(string + str(integer))
#term = string lateral , string concatenation, print statment, typecasting, length method len(vari),
#boolean has only True or False
#there are 4 basic datatypes: int,str,float,bool

multiple assignment :
    #1 -->
    vari1 , vari2, vari3, vari4 = "string",32,132.32,True
    #2 -->
    vari1 = vari2 = vari3 = vari4 = 30

#some method for string
len(vari) # will get length of the string
vari.find("0") #will get the index at which the character "0" is located within string
vari.capitalize() # capitalize only the first letter
vari.upper() # all the character will be capitalize
vari.lower() # vice versa
vari.isdigit() # checks wether the string contains only number
vari.isalpha() # checks wether the string contains only alphabetes
vari.count("o") # will count character 'o' within string 
vari.replace("o","a") #will replace all o character with a character
vari*3 # --> vari + vari + vari

#typecasting:
    print(int(32.32))

#user input
int(input("How old are you?: ")) #it will print the prompt first and then whatever the user types will be taken converted into int data type

#maths
import math
print(round(number)) # or we can use round()function using math.round()
print(ceil(number)) # will get largest closest integer of number
print(floor(number)) # will get smallest closest integer of number
print(abs(number)) # will find how far is the value from 0 (or in simpler terms its modulous)
print(sqrt(number)) # will find square root of the number
print(pow(number,integer_x)) # will get power of the number to the 
ower of integer_x
print(max(num1, num2, ..etc)) # will find the value which is maximum among the argument
print(min(num1, num2, ..etc)) # will find the value which is minimun among the argument

#string slicing --> creating substring by extracting elememts from another string
# we can use either indexing[] or slice()
#[start:stop:step]
name="Never gonna give you up!"
print(name[0]) # output- N
print(name[0:3]) # output- Nev 
print(name[6:5]) # output - gonna
print(name[:5]) # it will assume the start value 0 and if stop was empty then stop value=end of the string, output- Never
print(name[::1]) # output- Never gonna give you up
print(name[::-1]) # output- pu uoy evig annog reveN
#my method 
print(name[x:y:z]) # select the value from which you want to start extracting ,and then for y value how many elememts you want to extract add it to "x value" , for z value how many elements you want to skip forward in between + 1 (and for backward skip - 1)
#now using slice() --> used to create slice object to extract elements from string
#(start,stop,step)
slice1=slice(6,-13)
print(name[slice1]) #slice1 here is slice object it is reuseable , output- gonna

#if elif else statement --> its a block of code which executes if its condition is true
if condition :
    BlockOfCode
elif condition :
    BlockOfCode
else:
    BlockOfCode

#logical operator-->used to check if two or more confitional statement 
#(and , or , not)

#while loop -- unliminted iteration or limites iteration
usage:
name=None
while not name:
    name = input("Enter your name :")
print("Hello "+name)

#for loop -- limited iteration
usage:
for i in range(10):
    print(i) #this will print i values from 0 to 9
for i in range(50,101): #first argu is starting point inclusive and second argu is ending point and is exclusive
    print(i) #this will print i value from 50 to 100 
for i in range(50,101,2):
    print(i) #this will print i value from 50,52,54,56,58,60...
for i in "Bro Code":
    print(i) #each character from string will be printed on new line

#nested loop

#note using print(string,end='') will not move the cursor to new line

#loop control structure
#(break = breaks the loop entirely, continue = skip the iteration to next one, pass = does nothing and acts as a placeholder)

#list used to store multiple items in single variable
food = ["pani puri","puri pani","pan puri","pani pur"]
#we can change elemnets or add elements to list
food.append("ice cream") # add element to end of element
food.remove("hotdog") # removes specific element from list
food.pop()#removes the last element
food.insert(0,"niggesh") # adds element to that place
food.sort() # sort in alphabatic order
food.clear() # clears all the elements

#2D lists
sublist=[23,312,31,233,32]
sublist2=[423,423,4,42,42,4]
sublist3=[42,4242,546,243,241,42]
2dlist=[sublist,sublist2,sublist3]
print(2dlist[0][1]) #will print 312

#tuples -- collection of ordered and unchangeable
student = ("Niggesh",69,"None")
print(student.index(69)) #output will be 1
print(student.count("None")) #output will be 1
if "Niggesh" in student:
    print("who was in the pondicherry")
for x in student:
    print(x) #  output : Niggesh \n 69 \n None \n

#set = collection which is unordered , unindexed. No duplicate values
#is faste9xr than list if we want to checl wether a perticular element is present or not
utensils={"fork","spoon","knife","plate"}
for x in utensils:
    print(x) # output - spoon, plate,fork,knife (can be random order)
utensils.add("napkin")
utensils.remove("spoon")
utensils.clear()
utensils.update(set2) #adds element of another sets to it
dinner_table = utensils.union(set2) # add two sets to create a 3rd set 
print(utensils.difference(set2))#output -- will print elements of utensils which are not included in set2
print(utensils.intersection(set2))#output -- will print common elements of utensils and set2

#dictionary -- A changeable and unordered collection of unique key:value pairs fast because they use hashing, allow us to access a value quickly
capital = {'USA':'Washington DC'
            'China':'Beijing',
           'India':'New Delhi',
           'Russia':'Moscow'}
capital.update({'germany':'berlin'}) # this will edit existing key , if a key doesnt exist then it will add that add
capital.pop('China') #to remove this key:value
capital.clear()#clears all the key:value
print(capital['India']) # will print value of key India
print(capital.get('germany')) #safer way to get the value of key
print(capital.keys()) #prints all the keys
print(capital.values()) #print all the value
print(capital.items()) #print all the key:value
for key,value in capital.items():
    print(key,value) # print all the key and value each on new lline

# index operator [] = gives accees to sequence's element (str,list.tuples)
name="bro code"
name[0] # b 
name[0:3] # bro

#function
def hello(name1,name2,name3):
    print("Hello ",name1, "\nHello ",name2,"\nHello ",name3)
hello("Rothchild","Elon","Morgan")

#return statement
def niggesh():
    return "you are in pondicherry"

#keyword argument
def hello(name1,name2):
    print("ay tu ja re...")
hello(name2="Babu bhaiya",name1="Raju")

#nested function
print((str(input("enter here idoit :")))," is what you typed? \nWhat a loser")

#scope
language="English"
def display_lang():
    language="Spanish"
    print(language)
display_lang() # it will give priroties to local,enclosing,global,built-in
print(language)

# * (args) = parameter that will pack all arguments into a tuple usefull so that a funciton can accept a varying amount of positional arguments
def sumnum(*argssss):
    sum=0
    #if you wish to change the argument then you will need to create tuple and edit it
    argssss = list(argssss)
    argssss[0] = 0
    for i in argssss:
        sum += i 
    return sum
print(sumnum(1,2,3,4,5,6))

# ** (kwargs) = parameter that will pack all arguments into a dictionary , useful so that a function can accept a varying amount of keyword arguments
def hello(**kwargsss):
    print("Hello",end=" ")
    for key,value in kwargsss.items():
        print(value,end=" ")
hello(title="Mr.",firstname="Deez",lastname="Nuts")

#str.format() = optional method that gives users more control when displaying output
animal="cow"
item = "moon"
print("The {} jumped over the {}".format(animal,item))
print("The {0} jumped over the {1}".format(animal,item)) #postional argument
print("The {animal} jumped over the {item}".format(animal="cow",item="moon")) #keyword argument
text="The {} jumped over the {}"
print(text.format(animal,item))
name="Bro"
print("hello {:5} nice to meet you".format(name)) # hello Bro   nice to meet you
print("hello {:<5} nice to meet you".format(name)) # to left alginment the name variable
print("hello {:>5} nice to meet you".format(name)) # to right alginment the name variable
print("hello {:^5} nice to meet you".format(name)) # to center alginment between the padding
number=3.1442342
print("the number is {:.3f}".format(number)) # 3.144
number=1000
print("the number is {:,}".format(number)) #1,000
print("the number is {:b}".format(number)) #1111101000
{:o}{:X}{:E}

#randum numbers
import random
x= random.randint(1,10) #assigns a random value from 1-10 to x
y= random.random()
myList=['rock','paper','scissor']
z= random.choice(myList) # randomly choices rock paper scissor
cards = [1,2,3,4,5,6,7,8,9,j,k,q,a]
random.shuffle(cards) # shuffles the elements within cards

#exception handling =  event detected during the execution that interrupt the flow of progranm
try:
    numerator = input("Enter the numberator :")
    denominator = input("Enter the denominator :")
    result=numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("We can't divide any number with zero")
except ValueError as e:
    print(e)
    print("enter int only")
except Exception as e:
    print(e)
    print("something went wrong")
else:
    print(result) # all the exception will be checked before coming to else statement to print our final result
finally:
    print("this will always print even during errors")

#file detection
