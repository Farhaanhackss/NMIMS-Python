#program 1
fruits=["apple","banana","cherry","mango"]
print(fruits)
print(fruits[0])
print(fruits[-1])
print(fruits[1:3])


#program 2
numbers=[5,2,9,1]
numbers.append(20)
numbers.insert(1,100)
numbers.sort()
print(numbers)
numbers.remove(100)
print(numbers)
print("length:",len(numbers))


#program 3
point=(10,20)
print(point[0],point[1])

coordinates=(12.9,77.6)
lat,lon=coordinates  #tuple unpacking
print(lat,lon)
#point[0]=99


#program 4
my_list=[1,2,3]
my_tuple=(1,2,3)

my_list[0]=99
print("list after change:",my_list)
print("tupple stays same:",my_tuple)


#prac exercise
#1
numbers = [25, 10, 45, 7, 30]
# Assume the first element is both largest and smallest
largest = numbers[0]
smallest = numbers[0]
# Compare each element
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
# Display the result
print("Largest number:", largest)
print("Smallest number:", smallest)


#2
numbers = [10, 20, 30, 40, 50]
# Swap first and last elements
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print("List after swapping:", numbers)


#3
subjects = ("Python", "Mathematics", "English", "Physics", "Chemistry")
print("Subjects are:")
for subject in subjects:
    print(subject)