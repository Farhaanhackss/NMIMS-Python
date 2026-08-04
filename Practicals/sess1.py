#program 1
print("Hello,World!")
print("Welcome","to","python")
print("Welcome","to","python",sep="-")
print("No newline here....",end="")
print("continues on the same line")


#program 2
#this is a single line comment
print("this line runes") #inline comment explaining this
#this is multiline comment(docstring)
#often used to described what a file or function does
print("comments are ignored by python")


#program 3
a=10      #int
b=3.14    #float
c="NMIMS" #str
d=True    #bool
e=2+3j    #complex
f=None    #NoneType
for value in(a,b,c,d,e,f):
  print(value,"->",type(value))


#program 4
length=12
breadth=5
print("area of rectangle=",length*breadth)
print("perimeter of rectangle=",2*(length+breadth))


#prac exercise
#1
print("Name: Tanishka Mudaliar")
print("College: (Enter your college name)")
print("Course: FY BSc Applied Mathematical Computing")


#2
# Declaring variables
age = 18            # int
percentage = 85.5   # float
name = "Tanishka"   # str
is_student = True   # bool

# Printing data types
print(type(age))
print(type(percentage))
print(type(name))
print(type(is_student))