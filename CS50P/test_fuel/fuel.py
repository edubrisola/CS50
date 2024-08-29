def main():
    # Main function is not required to do anything specific in the instructions.
    pass


def convert(fraction):
    try:
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        if x > y:
            raise ValueError("Numerator cannot be greater than denominator.")
        percentage = round((x / y) * 100)
        return max(0, min(100, percentage))  # Ensure percentage is between 0 and 100
    except ValueError:
        raise ValueError("Invalid input. Ensure X and Y are integers and X <= Y.")
    except ZeroDivisionError:
        raise ZeroDivisionError("Denominator cannot be zero.")


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
