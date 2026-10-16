
                                                                             #5 Markers:


#Question 1: Q1. [Python Basics & Data Structures] Let letters = ["a", "b", "a", "c", "a", "d"]. Print how many times "a" occurs, the index of the first "c", and the list after removing the FIRST "a" only. [5 Marks] 
#Python Basics & Data Structures
letters = ["a", "b", "a", "c", "a", "d"]
print(letters.count("a"))
print(letters.index("c"))
letters.remove("a")
print(letters)
#output:
#3
#3
#['b', 'a', 'c', 'a', 'd']


#Question 2
# [Strings, I/O & Operators] Let x = 15. Using relational and logical operators, print whether (a) x lies between 10 and 20 using a chained comparison, (b) x is divisible by both 3 and 5, and (c) x is NOT even. [5 Marks]
#Strings, I/O & Operators
x = 15
print("(a) x lies between 10 and 20:", 10 < x < 20)          # chained comparison
print("(b) x divisible by both 3 and 5:", x % 3 == 0 and x % 5 == 0)
print("(c) x is NOT even:", not (x % 2 == 0))

#output:
#(a) x lies between 10 and 20: True
#(b) x divisible by both 3 and 5: True
#(c) x is NOT even: True


#Question 3 
#[Control Flow & Loops] Using a for loop with range(len(...)), print each character of the string "NMIMS" alongwith its index in the form "0 -> N". [5 Marks]
#Control Flow & Loops
s = "NMIMS"
for i in range(len(s)):
    print(f"{i} -> {s[i]}")

#Output 
#0 -> N
#1 -> M
#2 -> I
#3 -> M
#4 -> S



#Question 4
#[Functions] Write a function c_to_f(c) that returns the Fahrenheit value, and use it in a loop to print a table for 0,20, 40, 60, 80 and 100 degrees Celsius. [5 Marks]
#Functions
def c_to_f(c):
    return c * 9 / 5 + 32
print("\nCelsius\tFahrenheit")
for c in [0, 20, 40, 60, 80, 100]:
    print(f"{c}\t{c_to_f(c):.1f}")

      #output:
#Celsius	  Fahrenheit
#0	            32.0
#20	            68.0
#40	            104.0
#60             140.0
#80             176.0
#100	          212.0
