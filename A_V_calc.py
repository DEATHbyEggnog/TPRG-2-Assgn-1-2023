import math
import time

# Function to calculate the area of a rectangle
def area_rectangle(length, width):
    return length * width

# Function to calculate the area of a triangle
def area_triangle(base, height):
    return 0.5 * base * height

# Function to calculate the area of a circle
def area_circle(radius):
    return math.pi * radius * radius

# Function to calculate the volume of a sphere
def volume_sphere(radius):
    return (4/3) * math.pi * (radius ** 3)

# Function to calculate the volume of a cube
def volume_cube(side_length):
    return side_length ** 3

class ViewMenu:
    choice = "d"  # Default view initially

    @classmethod
    def view_menu(cls):
        print("Welcome to the Area and Volume Calculator")
        print("To view your formula and answer, press V/v for calculated view.")
        print("To view just the answer, press D/d for default view")

        while True:
            choice = input("Enter your preferred view format, or Q/q to quit: ").strip().lower()

            if choice == "v":
                print("You have chosen calculated view! How nice.")
                cls.choice = "v"
                time.sleep(2)
                break

            if choice == "d":
                print("You have chosen default view! Lovely")
                cls.choice = "d"
                time.sleep(2)
                break

            if choice == "q":
                print("Exiting program...Goodbye.")
                time.sleep(5)
                exit()

def calculate_and_display(title, formula, calculate_function, input_prompts, parameter_names):
    if not isinstance(input_prompts, list):
        input_prompts = [input_prompts]

    inputs = []
    for prompt in input_prompts:
        value = float(input(prompt))
        inputs.append(value)

    result = calculate_function(*inputs)
    calculate_string = f"{result:.2f}"

    formula_string = formula.format(*inputs)
    formula_with_params = f"{parameter_names} = {calculate_string}"

    print(f"Let's calculate the {title}!")
    if ViewMenu.choice == "v":
        print(f"{formula_string} = {calculate_string}  {formula_with_params}")
    else:
        print(f"{formula_string} = {calculate_string}")


def main():
    while True:
        print("Area and Volume Calculator")
        print("1. Calculate Area of Rectangle")
        print("2. Calculate Area of Triangle")
        print("3. Calculate Area of Circle")
        print("4. Volume of Sphere")
        print("5. Volume of Cube")
        print("Q. Press q to Quit")

        choice = input("Enter your choice (1-5, Q): ").strip().lower()

        if choice == "1":
            calculate_and_display("Area of Rectangle", "{:.2f} * {:.2f}", area_rectangle, ["What is the width, in cm? ", "What is the length, in cm?"], "Width x Length")
        elif choice == "2":
            calculate_and_display("Area of Triangle", "(1/2 * {:.2f} * {:.2f})", area_triangle, ["What is the base length, in cm? ", "What is the height, in cm?"], "Base x Height")
        elif choice == "3":
            calculate_and_display("Area of Circle", "π * {:.2f}²", area_circle, "What is the radius, in cm? ", "Radius²")
        elif choice == "4":
            calculate_and_display("Volume of Sphere", "4/3 * π * {:.2f}³", volume_sphere, "What is the radius, in cm? ", "Radius³")
        elif choice == "5":
            calculate_and_display("Volume of Cube", "{:.2f}³", volume_cube, "What is the side length, in cm? ", "Side Length³")
        elif choice == "q":
            print("Exiting program...Goodbye.")
            time.sleep(5)
            exit()
        else:
            print("You've chosen incorrectly")

if __name__ == "__main__":
    ViewMenu.view_menu()
    main()
