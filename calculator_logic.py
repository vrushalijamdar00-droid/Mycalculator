"""
Calculator Logic Module
"""


class Calculator:
    """Basic calculator operations"""

    @staticmethod
    def add(a: float, b: float) -> float:
        """Add two numbers"""
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Subtract second number from first"""
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers"""
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Divide first number by second"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    @staticmethod
    def modulus(a: float, b: float) -> float:
        """Return remainder"""
        if b == 0:
            raise ValueError("Cannot perform modulus by zero")
        return a % b

    @staticmethod
    def power(a: float, b: float) -> float:
        """Raise a to the power of b"""
        return a ** b


# Test the calculator when this file is run directly
if __name__ == "__main__":
    print("Addition:", Calculator.add(10, 5))
    print("Subtraction:", Calculator.subtract(10, 5))
    print("Multiplication:", Calculator.multiply(10, 5))
    print("Division:", Calculator.divide(10, 5))
    print("Modulus:", Calculator.modulus(10, 3))
    print("Power:", Calculator.power(2, 3))