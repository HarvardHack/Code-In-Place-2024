from graphics import Canvas

def main():
    # Create a canvas of size 400x400
    canvas = Canvas(400, 400)
    
    # Draw the first car at position (10, 10)
    x = 10
    y = 10
    draw_car(canvas, x, y)  # Pass canvas, x, and y to draw_car

    # Draw the second car at position (100, 100)
    x = 100
    y = 100
    draw_car(canvas, x, y)  # Pass canvas, x, and y to draw_car

def draw_car(canvas, x, y):
    # Draws a car at the given (x, y) location
    # The offsets for the rectangles are assumed to be correct
    canvas.create_rectangle(x, y, x + 50, y + 20)
    canvas.create_rectangle(x + 10, y - 10, x + 40, y + 20)

if __name__ == '__main__':
    main()
