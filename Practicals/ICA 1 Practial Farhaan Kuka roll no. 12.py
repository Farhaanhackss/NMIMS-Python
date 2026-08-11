#5 markers (Set 3) 

#Q1: let a = 5 and b = a. Now do b+= 3. Write the program and print both a and b. Observe and state ina comment whether changing b affected a. 

a  = 5 
b = a 
b += 3 
print (a) 
print (b) 

# Therefore, changing b does not affect a as b is a copy of the value 5.
#Output was a = 5 and b = 8 


#Q2: Write a program that safely checks the LENGTH of a string before accessing an index far into it so that it never raises an IndexError even if the requested index doesnt exist
def safe_access(s: str, index: int):
    return s[index] if 0 <= index < len(s) else None

if __name__ == "__main__":
    text = "hello"
    index = 10
    result = safe_access(text, index)
    print(result or f"Index {index} is out of range for string of length {len(text)}.")



#Q3: make a tuple and then turn it into a list and then add 10 in the place of the first element and then turn it into a tuple again. 
t = (1, 2, 3)

# Convert tuple to list to allow modification
l = list(t)

# Change the first element
l[0] = 10

# Convert back to tuple and print the result
result = tuple(l)
print(result)
#Output was (10, 2, 3)


#Q4: A = {1,2,3} and B = {2,3,4}. Print A^B (symmetric difference) and add a comment explaining what this operator returns

A = {1, 2, 3}
B = {2, 3, 4}
print(A ^ B)  
#returns the symmetric difference of the two sets 
#Outout was {1, 4}
