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
import os
path ="C:\\Users\\Desktop\\folder"
if os.path.exists(path): #checks wether the path exists and returns boolean value
    print("That location exists")
    if os.path.isfile(path): #checks if its file 
        print("This is a file")
    elif os.path.isdir(path):#checks if its directory
        print("This is directory")
else:
    print("That location doesnt exists")

#read content of file
try:
    with open("pathtotext.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")

#write a file
text="hello this is si ssisf afdjfjsncjsnf fjsnjxnc"
with open("pathtotext.txt","w") as file: #"w" for overwriting and "a" for append a file in python
    file.write(text)

#copy a file
#copyfile() = copies contents of a file
#copy()= copyfile()+permission mode+destination can be directory
#copy2()=copy()+copies metadata (file's creation and modication times)
import shutil
shutil.copyfile("pathtosource.txt","pathtodestination") # there are two arguments source and destination 

#move a file
import os
source="pathtosource"
destination="pathtodestination"
try:
    if os.path.exists(destination):
        print("this file already exists")
    else:
        os.replace(source,destination)
        print(source + "was moved")
except FileNotFoundError:
    print(source +"was not found")

#delete a file
import os
import shutil
path="test.txt"
try:
    os.remove(path) #removes files
    os.rmdir(path) # removes folder which is empty
    shutil.rmtree(path) # removes foler and the files it contains
except FileNotFoundError:
    print("This file doesnt exists")
except PermissionError:
    print("You donot have permission to delete that, the folder is empty")
except OSError:
    print("You cannot delete that using that function, the folder is not empty")
else:
    print(path + " was deleted")

#modules in python
#a module name message.py with contents in it:
def hello():
    print("hello how are you")
def bye():
    print("bye and have a nice day")
#now our main.py with contents in it:
import message #to import message module
message.hello() #when used import module , we have to use module.fucntion() to call its fuction
import message as msg #to import message as msg 
msg.hello() #it gets an alias name msg 
from message import hello,bye #to import hello and bye fuction from message.py
hello() # when used from module import fuction it will import those particular fucitons and can be called fuction()
from message import * #to import all the function from message.py
hello() # can all the fuction which are present in module 

#rock paper scissors
import random
options = ("rock", "paper", "scissors")
running = True
while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")
    print(f"Player: {player}")
    print(f"Computer: {computer}")
    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")
    if not input("Play again? (y/n): ").lower() == "y":
        running = False
print("Thanks for playing!")

#quiz game
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)
-------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
-------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")
-------------------------
def play_again():
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False
-------------------------
questions = {
 "Who created Python?: ": "A",
 "What year was Python created?: ": "B",
 "Python is tributed to which comedy group?: ": "C",
 "Is the Earth round?: ": "A"
}
options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]
new_game()
while play_again():
    new_game()
print("Byeee!")

#OOPs 
#object is an instance of a class by using programming we can create representation of reallife objects
#we can assign attributes to objects , example of attributes is name age height .etc
#we can assign methods to objects, think it of "action" like sleep eats gaming
#inorder to create object we need to create class , thinl of it as blueprint that describe what type of attributes and methods our distinct object will have
#file name main.py
from car import Car
car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")
print(car_1.model)
car_1.drive()
car_2.stop()
#------------------------------------------------------------------
#file name car.py
class Car: #car is a object and there are different cars like different shape, engine , color 
    def __init__(self,make,model,year,color): #its a special method that will construct objects for us (in other programming language this refers to as constructor) it contains unique attributes
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def drive(self): #here "self" refers to object that is using this method
        print("This "+self.model+" is driving")
    def stop(self):
        print("This "+self.model+" is stopped")

#class variable vs instance variable
#filename main.py
from car import Car
car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")
car_1.wheels = 2 
print(car_1.wheels) # output -- 2 
print(car_2.wheels) # output -- 4 
Car.wheels = 2 # this change will affect all instance of our class Car
print(car_1.wheels) #output -- 2 
print(car_2.wheels) # output -- 2
#--------------------
#filename car.py
class Car:
    wheels = 4 #class variable , it will be defualt value for all objects created by class Car , and it is changeable
    def __init__(self,make,model,year,color): #variable declared in constructor are instance variable
        self.make = make    #instance variable are unique for all the objects created by class Car
        self.model = model  #instance variable
        self.year = year    #instance variable
        self.color = color  #instance variable

#inheritance
class Animal:
    alive = True
    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")
class Rabbit(Animal): #by passing class as argument, we have now made 'Animal" a parent class of child class "Rabbit" , and it will inherit all the attributes and methods that parent class has
    def run(self):
        print("This rabbit is running")
class Fish(Animal):
    def swim(self):
        print("This fish is swimming")
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")
rabbit = Rabbit()
fish = Fish()
hawk = Hawk()
print(rabbit.alive)
fish.eat()
hawk.sleep()
rabbit.run()
fish.swim()
hawk.fly()

#multilevel inheritance --  when a derived (child) class has another derived (child) class
class Organism:
    alive = True
class Animal(Organism):
    def eat(self):
        print("This animal is eating")
class Dog(Animal):
    def bark(self):
        print("This dog is barking")
dog = Dog()
print(dog.alive)    # inherited from the Organism class
dog.eat()           # inherited from the Animal class
dog.bark()          # defined in Dog class

#multiple inheritance = when a child class is derived from more than one parent class
class Prey:
    def flee(self):
        print("This animal flees")
class Predator:
    def hunt(self):
        print("This animal is hunting")
class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey, Predator):
    pass
rabbit = Rabbit()
hawk = Hawk()
fish = Fish()
rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()

#method overriding
class Animal:
    def eat(self):
        print("This animal is eating")
class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot") #this will override the method of inherited class
rabbit = Rabbit()
rabbit.eat() 

#method chaining
#method chaining = calling multiple methods sequentially and each call performs an action on the same object and returns self
class Car:
    def turn_on(self):
        print("You start the engine")
        return self
    def drive(self):
        print("You drive the car")
        return self
    def brake(self):
        print("You step on the brakes")
        return self
    def turn_off(self):
        print("You turn off the engine")
        return self
car = Car()
car.turn_on().drive() #after adding return self in each methods this is how the code will work --> car.turn_on().drive --(after executing turn_on method it will return self which is car)--> car.drive
car.brake().turn_off()
#car.turn_on().drive().brake().turn_off()
#here '\' is line continuation character
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()

#super function
#super() = Function used to give access to the methods of a parent class. Returns a temporary object of a parent class when used
#super() gets the childe class to access to the attributes from the parents method,it doesnt override anything, but is useful when your child class needs the same attributes
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
class Square(Rectangle):
    def __init__(self, length, width): #this will pull lenght and width attributes from parent class
        super().__init__(length,width)
    def area(self):
        return self.length*self.width
class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length,width)
        self.height = height
    def volume(self):
        return self.length*self.width*self.height
square = Square(3, 3)
cube = Cube(3, 3, 3)
print(square.area())
print(cube.volume())

#abstract class = a class which contains one or more abstract methods.
#abstract method = a method that has a declaration but does not have an implementation.
#prevents a user from creating an object of that class + compels a user to override abstract methods in a child class
#by adding abstract method, your child class will have to overide it to acctucally work (when you add implementation for "go()" in child class, it will look for go () within child class before looking for parent class)
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def go(self):
        print("You drive the car")
    def stop(self):
        print("This car is stopped")
class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")
    def stop(self):
        print("This motorcycle is stopped")
#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()
#vehicle.go()
car.go()
motorcycle.go()
#vehicle.stop()
car.stop()
motorcycle.stop()

#objects as arguments
class Car:
    color = None
class Motorcycle:
    color = None
def change_color(vehicle,color):
    vehicle.color = color
car_1 = Car()
car_2 = Car()
car_3 = Car()
bike_1 = Motorcycle()
change_color(car_1,"red")
change_color(car_2,"white")
change_color(car_3,"blue")
change_color(bike_1,"black")
print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)

#duck typing
duck typing = concept where the class of an object is less important than the methods/attributes
class type is not checked if minimum methods/attributes are present
“If it walks like a duck, and it quacks like a duck, then it must be a duck.”
class Duck:
    def walk(self):
        print("This duck is walking")
    def talk(self):
        print("This duck is qwuacking")
class Chicken:
    def walk(self):
        print("This chicken is walking")
    def talk(self):
        print("This chicken is clucking")
class Person():
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")
duck = Duck()
chicken = Chicken()
person = Person()
person.catch(chicken)

#walrus operator 
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression
 happy = True
 print(happy) #output -- True
 print(happy := True) # output -- True
 foods = list() 
 while True:
   food = input("What food do you like?: ")
       if food == "quit":
           break
   foods.append(food)
foods = list() #now writing above code using walrus operator
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)

#functions to variable
def hello():
    print("Hello")
hi = hello
hi() #output -- Hello
say = print
say("Whoa! I can't believe this works! :O") #output -- Whoa! I cant believe this works! :O

#higher order functions
#  Higher Order Function =  a function that either:
#                           1. accepts a function as an argument
#                               or
#                           2. returns a function
#                           (In python, functions are also treated as objects)

# ----- 1. accepts a function as an argument ----- 
def loud(text):
   return text.upper()
def quiet(text):
   return text.lower()
def hello(func):
   text = func("Hello")
   print(text)
hello(loud)
hello(quiet)
# ------------ 2. returns a function ------------- 
def divisor(x):
   def dividend(y):
       return y / x
   return dividend
divide = divisor(2)
print(divide(10))

#lambda
# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
# lambda parameters:expression
double = lambda x: x * 2 #lambda argument:return'
print(double(1))
multiply = lambda x, y: x * y
print(multiply(1,2))
add = lambda x, y, z: x + y + z
print(add(1,2,3))
full_name = lambda first_name, last_name: first_name+" "+last_name
print(full_name("Bro","Code"))
age_check= lambda age:True if age >= 18 else False

#sort
# sort() method   = used with lists
# sort() function = used with iterables
students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick","D", 36),
            ("Spongebob","B", 20),
            ("Mr.Krabs","C", 78))
grade = lambda grades:grades[1]
# students.sort(key=age)                     # sorts current list
sorted_students = sorted(students,key=grade) # sorts and creates a new list
for i in sorted_students:
    print(i)

#map
# map() =   applies a function to each item in an iterable (list, tuple, etc.)
# map(function,iterable)
store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]
to_euros = lambda data: (data[0],data[1]*0.82)
# to_dollars = lambda data: (data[0],data[1]/0.82)this represents tuples
store_euros = list(map(to_euros, store))
for i in store_euros:
    print(i)

#filter
# filter() =    creates a collection of elements from an iterable,
#               for which a function returns true
#               filter(function, iterable)
friends = [("Rachel",19),
           ("Monica",18),
           ("Phoebe",17),
           ("Joey",16),
           ("Chandler",21),
           ("Ross",20)]
age = lambda data:data[1] >= 18
drinking_buddies = list(filter(age, friends))
for i in drinking_buddies:
    print(i)

#reduce
# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats process until 1 value remains
# reduce(function, iterable)
import functools
letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x, y,:x + y,letters)
print(word)
# factorial = [5,4,3,2,1]
# result = functools.reduce(lambda x, y,:x * y,factorial)
# print(result)

#list comprehensions
# list comprehension =  a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression if conditional else for item in iterable]
# --------------------------------------------------------------
squares = []                # create an empty list
for i in range(1,11):       # create a for loop
    squares.append(i * i)    # define what each loop iteration should do
print(squares)
# create a list AND defines what each loop iteration should do
squares = [i * i for i in range(1,11)]
print(squares)

#dictionary comprehensions
# dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda functions
# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}
# -------------------------------------------------------------------------
cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()
print(cities_in_C)
# -------------------------------------------------------------------------
# weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
# sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}
# print(sunny_weather)

#zip function
# zip(*iterables) =  aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                               creates a zip object with paired elements stored in tuples for each element
usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")
login_dates = ["1/1/2021","1/2/2021","1/3/2021"]
# --------------------------------------
users = list(zip(usernames,passwords))
for i in users:
    print(i)
# --------------------------------------
users = dict(zip(usernames,passwords))
for key,value in users.items():
    print(key+" : "+value)
# --------------------------------------
users = zip(usernames,passwords,login_dates)
for i in users:
    print(i)

#if _name_ =='__main__'
# ***********************************
# y tho?
# 1. Module can be run as a standalone program
#    or
# 2. Module can be imported and used by other modules
#  Python interpreter sets "special variables", one of which is __name__
#  Python will assign the __name__ variable a value of '__main__' if it's
#  the initial module being run
def main():
    print("Hello!")
if __name__ == '__main__':
    main()

#time module
import time
# ***************************************************************************
print(time.ctime(0))    # convert a time expressed in seconds since epoch to a readable string
#                                        epoch = when your computer thinks time began (reference point)
print(time.time())      # return current seconds since epoch
print(time.ctime(time.time())) # will get current time
# ***************************************************************************
# time.strftime(format, time_object) = formats a time_object to a string
# time_object = time.localtime() # local time
# time_object = time.gmtime()  # UTC time
# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
# print(local_time)
# ***************************************************************************
# time.strptime(string_string, format) = parses a string representing time/date and returns a struct_time object
# time_string = "20 April, 2020"
# time_object = time.strptime(time_string,"%d %B, %Y")
# print(time_object)
# ***************************************************************************
# time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and returns a string
# (year, month, day, hours, minutes, secs, #day​ of the week, #day​ of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.asctime(time_tuple)
# print(time_string)
# ***************************************************************************
# time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and return seconds since epoch
# (year, month, day, hours, minutes, secs, #day​ of the week, #day​ of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.mktime(time_tuple)
# print(time_string)

#threading
# thread =  a flow of execution. Like a separate order of instructions.
#                  However each thread takes a turn running to achieve concurrency
#                  GIL = (global interpreter lock),
#                  allows only one thread to hold the control of the Python interpreter at any one time
# cpu bound = program/task spends most of its time waiting for internal events (CPU intensive)
#                        use multiprocessing
# io bound = program/task spends most of its time waiting for external events (user input, web scraping)
#                     use multithreading
import threading
import time
def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")
def drink_coffee():
    time.sleep(4)
    print("You drank coffee")
def study():
    time.sleep(5)
    print("You finish studying")
x = threading.Thread(target=eat_breakfast, args=())
x.start()
y = threading.Thread(target=drink_coffee, args=())
y.start()
z = threading.Thread(target=study, args=())
z.start()
x.join()
y.join()
z.join()
print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())

#daemon threads
# daemon thread = a thread that runs in the background, not important for program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normally be killed, stay alive until task is complete
#                 ex. background tasks, garbage collection, waiting for input, long running processes
import threading
import time
def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ", count, "seconds")
x = threading.Thread(target=timer, daemon=True)
x.start()
# x.setDaemon(True)
# print(x.isDaemon())
answer = input("Do you wish to exit?")

#multiprocessing
# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)
from multiprocessing import Process, cpu_count
import time
def counter(num):
    count = 0
    while count < num:
        count += 1
def main():
    print("cpu count:", cpu_count())
    a = Process(target=counter, args=(500000000,))
    b = Process(target=counter, args=(500000000,))
    a.start()
    b.start()
    print("processing...")
    a.join()
    b.join()
    print("Done!")
    print("finished in:", time.perf_counter(), "seconds")
if _name_ == '__main__':
    main()

#gui windows 
from tkinter import *
window = Tk() #instantiate an instance of a window
window.geometry("420x420")
window.title("Bro Code first GUI program")
icon = PhotoImage(file='logo.png')
window.iconphoto(True,icon)
window.config(background="#5cfcff")
window.mainloop() #place window on computer screen, listen for events

#labels
from tkinter import *
# label = an area widget that holds text and/or an image within a window
window = Tk()
photo = PhotoImage(file='person.png')
label = Label(window,
              text="bro, do you even code?",
              font=('Arial',40,'bold'),
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')
label.pack()
#label.place(x=0,y=0)
window.mainloop()

#buttons
from tkinter import *
# button = you click it, then it does stuff
count = 0
def click():
    global count
    count+=1
    print(count)
window = Tk()
photo = PhotoImage(file='like.png')
button = Button(window,
                text="click me!",
                command=click,
                font=("Comic Sans",30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound='bottom')
button.pack()
window.mainloop()

#entrybox
from tkinter import *
#entry widget = textbox that accepts a single line of user input
def submit():
    username = entry.get()
    print("Hello "+username)
def delete():
    entry.delete(0,END)
def backspace():
    entry.delete(len(entry.get())-1, END)
window = Tk()
entry = Entry(window,
              font=("Arial",50),
              fg="#00FF00",
              bg="black")
#entry.insert(0,'Spongebob')
#entry.config(show="*")
#entry.config(state=DISABLED)
entry.pack(side=LEFT)
submit_button = Button(window,text="submit",command=submit)
submit_button.pack(side=RIGHT)
delete_button = Button(window,text="delete",command=delete)
delete_button.pack(side=RIGHT)
backspace_button = Button(window,text="backspace",command=backspace)
backspace_button.pack(side=RIGHT)
window.mainloop()


