def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)

        result = num / den

        print(f"The result of the division is {result}")
    except ZeroDivisionError:
        return "Cannot divide by zero"
    
    except ValueError:
        return "Error. Value must be a number"
    