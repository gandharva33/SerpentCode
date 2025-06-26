print("Welcome to Calculator!!")

print("Select an operation:")
print("1.Addition(+)")
print("2.Subtraction(-)")
print("3.Multiplication(*)")
print("4.Division(/)")

operation = input("Select and operation(+)(-)(*)(/):")

n1 = float(input("Enter number 1:"))
n2 = float(input("Enter number 2:"))

if operation == '+':
    print(f"{n1+n2}")

elif operation == '-':
    print(f"{n1-n2}")

elif operation == '*':
    print(f"{n1*n2}")

elif operation == '/':
    if n2 == 0:
        print("Error!! Can't divide by zero!")
    else:
        print(f"Result: {n1 / n2}")

else:
    print("Invalid operation selected!")

print("End of program...!")          
