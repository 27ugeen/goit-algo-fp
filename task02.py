import turtle

def draw_pythagorean_tree(t, length, angle, depth):
    if depth == 0:
        return
    t.forward(length)
    t.left(angle)
    draw_pythagorean_tree(t, length * 0.707, angle, depth - 1)
    t.right(angle * 2)
    draw_pythagorean_tree(t, length * 0.707, angle, depth - 1)
    t.left(angle)
    t.backward(length)

def main():
    # Ask the user for the recursion depth
    depth = int(input("Enter the recursion depth for the Pythagorean Tree fractal: "))

    # Initialize the turtle module and create a window
    screen = turtle.Screen()
    screen.title("Pythagorean Tree Fractal")
    screen.setup(width=800, height=600)
    screen.bgcolor("white")

    # Initialize the turtle and set its initial parameters
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.left(90)

    # Set the color of the tree
    t.color("green")  # Change "green" to any color you like

    # Call the function to draw the Pythagorean Tree fractal
    draw_pythagorean_tree(t, 100, 45, depth)

    # Keep the window open until the user clicks on it
    screen.mainloop()

if __name__ == "__main__":
    main()
