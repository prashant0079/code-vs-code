class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

if __name__ == "__main__":
    calc = Calculator()
    print("Welcome to Calculator!")
    # We keep the multiplication example, but the class now has all 3 capabilities
    print("Current feature: Multiplication")
    print("Example: 5 * 3 =", calc.multiply(5, 3))