#sum of two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum = num1 + num2
difference= num1-num2
print("Sum of these two numbers is : " , sum)
print("Difference of these two numbers is : " , difference)
print("product: ", num1*num2)
print("Division: ", num1/num2)
print("Floor Division: ", num1//num2)
print("Remainder: ", num1%num2)
print("Exponentiation: ", num1**num2)

#logical operators
exp1 = 2 > 1
exp2 = 5 < 4
print("exp1 and exp2 :", exp1 and exp2)
print("exp1 or exp2 :", exp1 or exp2)
print(" not of exp1 :", not(exp2) )

#identity operators
x = 5
y = 5
print("if x is y :",x is y)
print("if x is not y :",x is not y)

#membership operators
fruits = ["apple", "banana , cherry"]
print("if banana is present in fruits:", "banana" in fruits)
print("if mango is not present in fruits:", "mango" not in fruits)

#bitwise operator
a = 5
b = 3
print("a and b:", a & b) 
print("a or b:", a | b) 
print("a xor b:", a ^ b) 