from graphics import Canvas

# Constants for the canvas dimensions
CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

def main():
    # Create a canvas with the specified width and height
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Coordinates for the red rectangle
    left_x = 0
    top_y = 0
    right_x = CANVAS_WIDTH
    bottom_y = CANVAS_HEIGHT // 2  # Half the height of the canvas
    
    # Draw the red rectangle
    rect = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'red')

if __name__ == '__main__':
    main()
