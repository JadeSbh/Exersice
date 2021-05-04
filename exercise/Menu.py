def area_circle(radius):
    return 3.14 * radius * radius


def area_triangle(height, base):
    return (height*base) / 2


def area_rectangle(width, height):
    return width * height


def get_pos_float(prompt):
    while True:
        try:
            x = float(input(prompt))
            if x <= 0:
                print(f" Sorry, you entered {x}, please enter a number greater than zero")
            else:
                return x
        except ValueError:
            print("your entry is not valid, please enter a valid number")


def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            print("Oh Sorry, please enter a valid number!")


menu = """ 
Choose an option:
1.area of a circle 
2.area of a rectangle
3.area of a triangle
0. quit
"""
while True:
    print(menu)
    choice = get_int("Please make your choice! Enter 1, 2, 3 or 0 :  ")
    if choice == 1:
        print("you choose to calculate the area of a circle is ")
        r = get_pos_float("Please, enter the radius:  ")
        area = area_circle(r)
        print(f" the area of a circle with radius equal to {r} is {area}.")
    elif choice == 2:
        print(" you choose to calculate the area of rectangle ")
        w = get_pos_float("please, enter the width of the rectangle")
        h = get_pos_float("please, enter the height of the rectangle")
        area = area_rectangle(w, h)
        print(f"The area of a rectangle with width equal to {w} and a height equal to {h} is {area}")
    elif choice == 3:
        print("you choose to calculate the area of triangle")
        h = get_pos_float("please, enter the height of the triangle:  ")
        b = get_pos_float("please, enter the base of the triangle:  ")
        area = area_triangle(h, b)
        print(f"The area of a triangle with height equal to {h} and a base equal to {b} is {area}")
    elif choice == 0:
        print("Good bye! See You Soon!")
        break
    else:
        print("Invalid choice, please choose from the menu 1, 2 or 0")