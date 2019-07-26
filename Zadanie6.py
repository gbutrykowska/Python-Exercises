class Calculator(object):

    def add(number1, number2):
        return float(number1) + float(number2)

    def substract(number1, number2):
        return float(number1) - float(number2)

    def multiply(number1, number2):
        return float(number1) * float(number2)

    def divide(number1, number2):
        return float(number1) / float(number2)

number1 = input("Please type in first number: ")
number2 = input("Please type in second number: ")

dzielenie_testowe = Calculator.divide(number1, number2)
print(dzielenie_testowe)
