from graphics import Canvas
import random

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH = 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base

def draw_pyramid(canvas):
    for row in range(BRICKS_IN_BASE):
        bricks_in_row = BRICKS_IN_BASE - row
        row_y = CANVAS_HEIGHT - (row + 1) * BRICK_HEIGHT
        offset_x = (CANVAS_WIDTH - bricks_in_row * BRICK_WIDTH) / 2
        
        for brick in range(bricks_in_row):
            x = offset_x + brick * BRICK_WIDTH
            y = row_y
            canvas.create_rectangle(x, y, x + BRICK_WIDTH, y + BRICK_HEIGHT, fill=random_color())

def random_color():
    return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_pyramid(canvas)
    canvas.mainloop()

if __name__ == '__main__':
    main()
