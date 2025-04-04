class Calculator:
    def __init__(self, name='user_calculator'):
        self.name = name
        self.memorized_operations = []


    def add(self, num1, num2):
        result = num1 + num2
        message = f'added {num1} to {num2} got {result}'
        self.memorized_operations.append(message)
        print(message)

    
    def subtract(self, num1, num2):
        result = num1 - num2
        message = f'subtracted {num1} from {num2} got {result}'
        self.memorized_operations.append(message)
        print(message)


    def multiply(self, num1, num2):
        result = num1 * num2
        message = f'multiplied {num1} with {num2} got {result}'
        self.memorized_operations.append(message)
        print(message)


    def divide(self, num1, num2):
        if num2 == 0:
            print('You cant divide by zero')
        else:
            result = num1 / num2
            message = f'divided {num1} by {num2} got {result}'
            self.memorized_operations.append(message)
            print(message)


calc = Calculator()
calc.subtract(1, 3)

