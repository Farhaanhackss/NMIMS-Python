#program  1
A={1,2,3,4}
B={3,4,5,6}

print("union:",A|B)
print("intersection:",A&B)
print("difference:",A-B)

A.add(10)
print("after add:",A)

#program 2
numbers=[4,8,4,6,8,2,6,1]
unique_numbers=list(set(numbers))
print("original:",numbers)
print("unique:",sorted(unique_numbers))

#program 3
student={"name":"Tanishka","age":18,"course":"Bsc amc"}
print(student["name"])
student["age"]=19
student["college"]="NMIMS"
print(student)
for key,value in student.items():
  print(key,"->",value)

#program 4
sentence="the cat sat on the mat the cat ran" 
words=sentence.split()
frequency={}
for word in words:
 frequency[word]=frequency.get(word,0)+1
print(frequency)

#prac exercise
#1
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
if A & B:
    print("The sets have common elements.")
    print("Common elements are:", A & B)
else:
    print("The sets have no common elements.")

#2
students = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 78,
    "Neha": 95,
    "Riya": 88
}
topper = max(students, key=students.get)
print("Topper:", topper)
print("Marks:", students[topper])