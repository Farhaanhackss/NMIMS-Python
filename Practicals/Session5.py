username = 129041
password = 1241
input("enter your username: ")
input("enter your password: ")
if username == 129041 and password == 1241: 
  print("access granted")
else:
  print("access denied") 
input("enter your SAP ID: ")
input("enter your roll no: ")

#Bill construction
items = input("What items have you bought? ")
qty = int(input("How much have you bought? "))
price = float(input("How much did the good cost? "))

total = qty * price

print(f"{'Item':<15} {'Quantity':<10} {'Price':<10} {'Total':<10}")
print("-" * 50)

print(f"{items:<15} {qty:<10} {price:<10.2f} {total:<10.2f}")

#Check divisibility
num = int(input("enter a number"))
if num % 3 == 0 and num % 5 == 0:
  print("is div") 
else:
  print("is not div") 

#listing marks & finding cumulative % 

allmarks = []
total_marks = 0

for i in range(1, 6):
    marks = int(input(f" Enter marks for subject {i}: "))
    if marks < 0 or marks > 100:
        print("Invalid marks. Marks should be between 0 and 100.")
        continue
    allmarks.append(marks)
    
    total_marks += marks
    cumulativepct = (total_marks / (i * 500)) * 100
    print(f"Cumulative Percentage after subject {i}: {cumulativepct:.2f}%")

print("Final marks list:", allmarks)
print(f"Final cumulative percentage: {(sum(allmarks) / 500) * 100:.2f}%")

