"""
Submitted By: Vaibhav Hooda (C0806432)
"""

import area
import date
import string_manipulation


def menu():

    print("Welcome to the utility program: \n"
          "1. Compute area of a circle.\n"
          "2. Display name in reverse order.\n"
          "3. Display current Date/Time.\n"
          "Press * to exit")

    choice = input("Please enter your choice: ")

    if choice == "1":
        area.compute_area()
    elif choice == "2":
        string_manipulation.reverse_name()
    elif choice == "3":
        date.display_date_time()
    elif choice == "*":
        exit()
    else:
        print("Invalid choice, please try again......")
    menu()


if __name__ == '__main__':
    menu()
