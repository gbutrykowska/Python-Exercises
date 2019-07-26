class Calculator(object):

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def add(number1, number2):
        sum = float(number1) + float(number2)
        return sum

    def substract(number1, number2):
        substraction = float(number1) - float(number2)
        return substraction

    def multiply(number1, number2):
        multiplication = float(number1) * float(number2)
        return multiplication

    def divide(number1, number2):
        division = float(number1) / float(number2)
        return division


number1 = (input("Please type in first number: "))
number2 = (input("Please type in second number: "))

dzielenie_testowe = Calculator.divide(number1, number2)
print(dzielenie_testowe)
