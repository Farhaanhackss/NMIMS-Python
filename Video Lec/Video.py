#list,tuples,set & dictinary
#int->whole numbers(no decimal point)
age=38
print(age)
print(type(age))

#floating point(decimal point)
height=5.8
print(height)
print(type(height))

#string types=text/nymbers-alphanumeric
stud_name="tanishka"
print(stud_name)
print(type(stud_name))

#boolean->2 values->True or False
is_stud=True
print(is_stud)
print(type(is_stud))
#age=38
#if age>30:
#  print(True)
#  print(type(True))
#else:
#  print(False)
#  print(type(False))
a=10; b=20;
print(a==b)
print(type(a==b))

#type checking
print(type(height))
print(type(stud_name))
print(type(is_stud))

#type casting (type conversion)
#int->string
num=5
result="hello"+str(num)
result1="hello",num
print(result)
print(type(result1))

#float<->int conversion
height=5.8
print(int(height))
print(float(height))

#string methods->upper(),lower(),count()
text="hello"
new_text=text.upper()
print(new_text)

#operators->basic
#1.Arithmetic operators-> +,-,/,*,//,%,**
#2.Comparison operators-> ==,!=,>,<,<=,>=
#3.Logical operators-> and, or, not

a=5
b=10
#Arithmetic operators
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) #floor div->it removes decimal point
print(21/5)
print(21//5)
print(10%5) #provides remainder
print(12**3) #power

#comparison operators->output always in boolean(T/F)
a=20
b=20
print(a==b)
print(a!=b)

#string comparison(case sensitive)
str1="Tanishka"
str2="tanishka"
print(str1==str2)
print(str1!=str2)

#greater than(>) & less than(<) & greater than equal to
#x=45
#y=55
#print(x<y)
#print(x>y)
#print(x<=y)
#print(x>=y)
per=17.99
if(per>18):
  print(True)
else:
  print(False)


#logical operators
x=True
y=False
print(x and y) #if both is true output is true
print(x or y)#if anyone condition is true->output is true
print(not x)#boolean value reverse

#mini project
num1=int(input("enter first number..."))
num2=int(input("enter second number..."))

print("addition=",num1+num2)
print("subtraction=",num1-num2)
print("multiplication=",num1*num2)
print("division=",num1/num2)
print("floor division=",num1//num2)
print("remainder=",num1%num2)

#conditional statement->decision making
#voting eligibility
age=20
if age>=18:
  print("eligible for voting")
else:
  print("not eligible for voting")


age=20
if age<13:
  print("you're a child")
elif age<18:
  print("you're a teenager")
else:
  print("you're an adult")

  #nested conditions
num=int(input("enter a number..."))
if num>0:
  print("positive number")
  if num%2==0:
    print("even number")
  else:
    print("odd number")
else:
  print("number is zero or negative")


  #leap year
#1.year divible by 4
#2.but divisible by 100->not a leap year
#3.but divisible by 100 400->leap year

year=int(input("enter a year..."))
#grand parent
if year%4==0:
  #parent if
  if year%100==0:
    #child if
    if year%400==0:
      print("leap year")
    else:
      print("not a leap year") # Divisible by 100 but not 400
  else:
    print(year,"is a leap year") # Divisible by 4 but not 100
else:
  print(year,"not a leap year") # Not divisible by 4


  #calc->if elif

num1=int(input("enter first num.."))
num2=int(input("enter second num.."))
op=input("enter operator..")

if op=="+":
  print("addition=",num1+num2)
elif op=="*":
  print("multiplication=",num1*num2)
elif op=="/":
  if num2!=0:
    print("division=",num1/num2)
  else:
    print("division not possible")
else:
  print("invalid operator")


  #practice questons
age=int(input("enter ur age.."))

if age < 5:
  print("invalid age")
elif age < 12:
  print("invalid age")
elif age < 18:
  is_student=input("are u a student?(yes/no)")
  if is_student=="yes":
    print("12 rupees")
  else:
    print("15 rupees")
elif age >= 60 and age <= 100:
  print("10 rupees")
elif age >= 60:
  print("50 rupees")
else:
  print("invalid age")