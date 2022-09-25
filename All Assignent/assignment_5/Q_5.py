#5. Write a python script which takes a three digit number from the user and displays
#only its first digit.

x = int(input("Enter three digit number only"))
z= x%10
t = x//100
print(z) # This is from write side 
print(t) # This is from left side 