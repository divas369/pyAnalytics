# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 17:19:35 2021

@author: divas
"""
#fn1

def greet(who="Colin"):
    print("Hello,", who)
    
greet()
greet(who="Kaggle")
# (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
greet("world")

#fn2
def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)
least_difference(1, 10, 100)

#fn3
def round_to_two_places(num):
   
    
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    return round(num,ndigits=2)
round_to_two_places(3.14159)


#fn of fn1
def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1), 
    sep='\n', # '\n' is the newline character - it starts a new line
)

#fn of fn2
def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)
True or False #and is evaluated before or

#Conditionals
def inspect(x):
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is negative")
    else:
        print(x, "is unlike anything I've ever seen...")

inspect(0)
inspect(-15)

#Boolean1
def is_odd(n):
    return (n % 2) == 1

print("Is 100 odd?", is_odd(100))
print("Is -1 odd?", is_odd(-1))


#Boolean2
def can_run_for_president(age, is_natural_born_citizen):
    """Can someone of the given age and citizenship status run for president in the US?"""
    # The US Constitution says you must be a natural born citizen *and* at least 35 years old
    return is_natural_born_citizen and (age >= 35)

print(can_run_for_president(19, True))
print(can_run_for_president(55, False))
print(can_run_for_president(55, True))

#Father- Retired Sergeant (Indian Air Force), currently working as a Mathematics professor in Priyadarshini Indira Gandhi Govt. College, Jind
#Mother- Homemaker  
#Throughout my childhood, I was very passionate about flying like a bird by developing some kind of wings. I watched a lot of videos on youtube about the same, Most of them leads to the discovery of an Aeroplane.
#1. I used to write poems during Lockdown, One of them got selected in an Anthology- Art of being human.
#2. I learnt Pencil sketching during Lockdown. The first sketch I made is of Nikola Tesla and it was admired by many.
#3.During my College days, I used to go to Gym. It introduced a discipline in my life.  
#3rd rank in Mechanisms and Robotics during ME.
#My current favorite subject is Data Analytics. I have done a  course from Henry Harvin Education on the same. 
#I was not good at handling my expenses. For instance, I like  shopping, eating good food which is very hygienic. All these habits lead to running out of balance at times.
#Sometimes, these things put extra burden on parents who are also paying huge college fees. That's why, I used to run tuition classes during my graduation.        


#I have chosen a project on machine learning. But I had no prior knowledge of the topic. So, initially I faced some problems to start it from scratch. But after googling and doing some course on Udemy, I become able to complete it in a good way. Also scored grade A for the same.

#I have seen that the company is focused on providing every facility to the employee, If he/she wants to work on some new technology. This is the best value I felt.

#I like to face new challenges, to learn new things at work in the given time. I wish to work for the society by discovering something that can be useful for the mankind. Also I feel the same thing is possible by working practically on the things.

#1. Effect of Location of Buildings on Cooling Load due to Sun’s Path using EnergyPlus. 2.Prediction of Energy Consumption of Lathe Machine using Gaussian Process Regression. 3.Dynamic Mode Decomposition and its Applications in Fluid Dynamics. 4.Simulation of Flow inside a Pulsating Heat Pipe.






















