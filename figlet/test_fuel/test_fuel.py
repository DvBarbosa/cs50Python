def convert(fraction):
    """
    Converts a fraction string in X/Y format to a percentage rounded to the nearest int between 0 and 100, inclusive.
    Raises a ValueError if X and/or Y is not an integer, or if X is greater than Y.
    Raises a ZeroDivisionError if Y is 0.
    """
    try:
        x, y = map(int, fraction.split('/'))
    except ValueError:
        raise ValueError("Invalid fraction string: {}".format(fraction))
    if x > y:
        raise ValueError("Invalid fraction: {}. X cannot be greater than Y.".format(fraction))
    if y == 0:
        raise ZeroDivisionError("Invalid fraction: {}. Y cannot be 0.".format(fraction))
    return round(x/y * 100)


def gauge(percentage):
    """
    Returns a string representing the fuel gauge based on the percentage.
    If percentage is less than or equal to 1, returns "E".
    If percentage is greater than or equal to 99, returns "F".
    Otherwise, returns "Z%", where Z is the percentage.
    """
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return "{}%".format(percentage)


def main():
    """
    Prompts the user for a fuel level and displays the corresponding gauge.
    """
    fuel_level = input("Enter the fuel level in X/Y format: ")
    try:
        percentage = convert(fuel_level)
        gauge_level = gauge(percentage)
        print("Fuel gauge: {}".format(gauge_level))
    except (ValueError, ZeroDivisionError) as e:
        print("Error: {}".format(str(e)))
