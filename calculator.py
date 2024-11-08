print("Welcome to Calculator Project")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
option = int(input("Select an option for Basic Operation : "))

if option == 1:
    n1 = int(input("Enter 1st Number : "))
    n2 = int(input("Enter 2nd Number : "))
    result = n1 + n2
    print("Your addition result : ", result)
elif option == 2:
    n1 = int(input("Enter 1st Number : "))
    n2 = int(input("Enter 2nd Number : "))
    result = n1 - n2
    print("Your Subtraction result : ", result)

elif option == 3:
    n1 = int(input("Enter 1st Number : "))
    n2 = int(input("Enter 2nd Number : "))
    result = n1 * n2
    print("Your Multiplication result : ", result)
elif option == 4:
    n1 = int(input("Enter 1st Number : "))
    n2 = int(input("Enter 2nd Number : "))
    result = n1 / n2
    print("Your Division result : ", result)
else:
    print("Invalid Input .... try again !!!")

