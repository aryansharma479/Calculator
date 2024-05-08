#Calculator
from art import logo

print(logo)


def calculator():

  #ADDITION
  def add(n1, n2):
    return n1 + n2

  #SUBTRACTION
  def sub(n1, n2):
    if n1 > n2:
      return n1 - n2
    else:
      return n2 - n1

  #MULTIPLICATION
  def mul(n1, n2):
    return n1 * n2

  #DIVISION
  def div(n1, n2):
    return n1 / n2

  #EXPONENTIAL
  def expo(n1, n2):
    return n1**n2

  operations = {
      "+": add,
      "-": sub,
      "*": mul,
      "/": div,
      "^": expo,
  }
  num1 = float(input("Enter Number First: "))
  for Symbol in operations:
    print(Symbol)
  shouldContinue = True
  while shouldContinue:
    op_symbol = input("Pick The Operation Symbol From Above: ")
    num2 = float(input("Enter New Number: "))
    cal_func = operations[op_symbol]
    ans = cal_func(num1, num2)
    print(f"{num1}{op_symbol}{num2}={ans}")
    ques = input(
        f"Type 'y' To Continue With The {ans} or Type 'n' To Start New Calculation. : "
    ).lower()
    print()
    if ques == 'y':
      num1 = ans
    else:
      shouldContinue = False
      calculator()


calculator()
