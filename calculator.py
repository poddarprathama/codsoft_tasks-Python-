print("Welcome to the PYTHON calculator!!")
a = float(input("Enter the 1st number: "))
b = float(input("Enter the 2nd number: "))
print()
print("Choose + for Addition")
print("Choose - for Subtraction")
print("Choose * for Multiplication")
print("Choose / for Divison")
print("Choose % for Modulation")

operator = input("Enter any operator:")
if operator == "+":
    sum = a+b
    print("The result is:",a+b)
elif operator == "-":
    subtraction = a-b
    print("The result is:",a-b)
elif operator == "*":
    multiplication = a*b
    print("The result is:",a*b)
elif operator == "/":
    divison = a/b
    print("The result is:",a/b)
elif operator == "%":
    modulation = a%b
    print("The result is:",a%b)
else:
    print("Invalid operator...")

print()
print("Thanks for using PYTHON calculator")



