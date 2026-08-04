#program 1
word="PYTHON"
print(word[0],word[-1])
print(word[1:4])
print(word[::-1])
print(len(word))


#program 2
name="Tanishka Mudaliar"
print(name.strip())
print(name.strip().upper())
print(name.strip().lower())
print(name.strip().replace("Tanishka","Tan"))
print(name.strip().split(" "))


#program 3
name=input("Enter your name:")
age=int(input("Enter your age:"))
print("Hello,",name,"-next year you will be",age+1)


#program 4
text=input("Enter a word:").lower().replace(" "," ")
if text==text[::-1]:
  print("it is a palindrome")
else:
  print("it is not a palindrome")


#prac exercise
#1
text=input("Enter a string:")
count=0
for ch in text:
  if ch.lower() in "aeiou":
    count+=1
print("Number of vowels:",count)


#2
str1=input("Enter the first string:")
str2=input("Enter the second string:")
result=str1+" "+str2
print("Concatenated string:",result)