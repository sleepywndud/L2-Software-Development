"""
This program makes a box of stars (*) in the dimensions that the user specified.
13.03.2026 James Park
"""


def box_horizontal(horizontal):
    """This function generates a row of stars in the dimension that the user specified."""
    print("")  # newline to increase visiblity of box

    # Printing the horizontal (horizontal) of the box
    for i in range(horizontal):
        print("*", end="")


def box_vertical(vertical):
    # Priting the vertical (vertical) of the box
    for i in range(vertical - 2):
        print("\n*" + (" " * (horizontal - 2)) + "*", end="")


horizontal = int(input("Enter the (horizontal) horizontal of the box: "))
vertical = int(input("Enter the (vertical) vertical of the box: "))

box_horizontal(horizontal)  # top horizontal section of box
box_vertical(vertical)
box_horizontal(horizontal)  # bottom horizontal section of box

print(f"\n\n{horizontal}x{vertical} Box Generated!")
