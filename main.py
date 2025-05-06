def calcultor():
  while True:
    num1 = float(input("Enter a number: "))
    operator = input("choose an operator(+,-,*,/):  ")
    num2 = float(input("Enter a Number: "))

    if(operator == "+"):
      result = num1 + num2
    elif(operator == "-"):
      result = num1 - num2
    elif(operator == "*"):
      result = num1 * num2
    elif(operator == "/"):
      if(num2 == 0):
        print("Cannot Divide with zero")
        continue
      else:
        result = num1 / num2

    else: 
      print("Invalid operation")
      continue

    print(result)

    again = input("Do You want to calculate agein(Y/N): ")
    if(again.upper() != "Y"):
      break

calcultor()