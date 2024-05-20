class MathService:
    def factorial(self, number: int = 0):
        if number < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if number == 0:
            return 1
        return number * self.factorial(number - 1)
