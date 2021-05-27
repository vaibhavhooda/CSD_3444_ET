"""
File used for area computation.
"""

# Constant
PI = 3.14


def compute_area():
    radius = input("Please enter the radius of circle: ")
    try:
        radius = float(radius)
    except ValueError:
        print("Non numeric value entered, Terminating.....")
        exit()

    area = PI * radius * radius
    print(f"Area of the circle with radius{radius} is: {area}")
