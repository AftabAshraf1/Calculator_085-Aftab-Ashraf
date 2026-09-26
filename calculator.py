print("My Calculator")

operate = input("What operation do you want to apply (+, -, *, /): ")

number1 = float(input("Enter your first number: "))
number2 = float(input("Enter your second number: "))

if operate == "+":
    print("Answer is", number1 + number2)

elif operate == "-":
    print("Answer is", number1 - number2)

elif operate == "*":
    print("Answer is", number1 * number2)

elif operate == "/":
    if number2 != 0:
        print("Answer is", number1 / number2)
    else:
        print("Cannot divide by zero")

else:
    print("Choose the Correct Option:")