List1 = [["python"], ["program"], ["example"]]
for i in List1: 
  for j in i: 
    for l in j:
      print(l)



num = int(input("Enter a number: ")) 
original = num
total = 0 
while num > 0:
  digit = num % 10 
  total += digit 
  num = num // 10
print(f"sum of digits of {original} = {total}")

count = 1 
while count <= 10:
  print(count)
  count += 1 

count = 1 
while True: 
  print(count)
  count += 1 
  if not (count <= 10): 
    break 

x = int(input("enter your number: ")) 
count = 1 
while count <= 10:
  t = count * x 
  print(t)
  count += 1


x = int(input("enter the number: ]")) 
secret = 7
if x == secret:
  print("WAOOOOO BADHAI HO") 
elif x > secret: 
  print("Bohot zyada") 
elif x < secret:
  print("bohot kam") 


year = int(input("Enter the year: ")) 
if year % 4 == 0: 
  print(f"{year} is a leap year") 
else: 
  print(f"{year} is not a leap year")
