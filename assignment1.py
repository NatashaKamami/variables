#Coding Challenge 1.1
# Question 1
num1 = int(input("First number:")) #Prompts a user for their first number
num2 = int(input("Second number:")) #Prompts a user for their second number
op = input("Operator:") #Prompts a user for their operator

if op == '+':
    result = num1 + num2 #explains what result is expected if the '+' operator is inputed
elif op == '-':
    result = num1 - num2 #explains what result is expected if the '-' operator is inputed
elif op == '*':
    result = num1 * num2 #explains what result is expected if the '*' operator is inputed
elif op == '/':
    result = num2 / num1 #explains what result is expected if the '/' operator is inputed
print(result) #prints the result after inputing your two numbers and the operator 

#Question 2
import random
print(random.randint(1, 100)) #randint generates a random number(integer) in the specified range in our case between 1 and 100

#Question 3
import math
print(math.sqrt(169))


#1.2 Exercises
#Question 1
name = input("Enter your name:") 
print("Hello",name)

#Question 2
hours = input("Ënter your hours:")
rate = input("Enter your rate per hour:")
pay = float(hours) *  float(rate)
print(pay)

#Question 3
width = 17
height = 12.0

print(width//2)
print(type(width//2))

print(width/2.0)
print(type(width/2.0))

print(height/3)
print(type(height/3))

print(1 + 2 * 5)
print(type(1 + 2 * 5))

#Question 4
temp = input("Temperature in Celcius:")
new_temp = (float(temp) * 1.8)  + 32
print(new_temp)