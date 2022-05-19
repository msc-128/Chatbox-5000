def calc():
  invalidInput = True
  while invalidInput:
    invalidInput = False
    try:
      num1 = float(input("Enter your first number\n> "))
    except:
      print("Please enter a number")
      invalidInput = True
      continue
    op = input("Would you like to add, subtract, multiply or divide? (+, -, *, /)\n> ")
    try:
      num2 = float(input("Enter your second number\n> "))
    except:
      print("Please enter a number")
      invalidInput = True
      continue
    if op == "+":
      print(num1 + num2)
    elif op == "-":
      print(num1 - num2)
    elif op == "*":
      print(num1 * num2)
    elif op == "/":
      print(num1 / num2)
    else:
      invalidInput = True
      print("Error: invalid input")
