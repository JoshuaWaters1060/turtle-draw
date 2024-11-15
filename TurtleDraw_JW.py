import turtle
import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def main():
    screen = turtle.Screen()
    screen.setup(450, 450)
    screen.title("Turtle Drawing Application")

    Jeremy = turtle.Turtle()
    Jeremy.speed("fastest")
    Jeremy.penup()

    input_file_name = input("Enter the name of the input file: ")

    try:
        with open(input_file_name, "r") as file:
            total_distance = 0
            last_x, last_y = None, None
            pen_down = False

            for line in file:
                line = line.strip()

                if line == "stop":
                    Jeremy.penup()
                    pen_down = False
                    continue

                parts = line.split()
                if len(parts) != 3:
                    print(f"Invalid line format: {line}")
                    continue

                color, x_str, y_str = parts
                try:
                    x, y = int(x_str), int(y_str)
                except ValueError:
                    print(f"Invalid coordinates: {x_str}, {y_str}")
                    continue

                Jeremy.pencolor(color)

                Jeremy.goto(x, y)
                if pen_down:
                    if last_x is not None and last_y is not None:
                        total_distance += calculate_distance(last_x, last_y, x, y)
                else:
                    Jeremy.penup()

                Jeremy.pendown()
                pen_down = True
                last_x, last_y = x, y

        Jeremy.penup()
        Jeremy.goto(200, -200)
        Jeremy.write(f"Total distance: {total_distance:.2f}", align="right", font=("Arial", 12, "normal"))

        input("Press Enter to close the window...")

    except FileNotFoundError:
        print(f"File not found: {input_file_name}")

    finally:
        screen.bye()

if __name__ == "__main__":
    main()
