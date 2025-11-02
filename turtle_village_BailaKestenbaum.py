# Turtle Village — Lite (Student Scaffold)
# Focus: loops, decisions, try/except, and small functions.
# Run this file locally (IDLE/Thonny/PyCharm).

# ===>>>  REMOVE PASS IN ALL METHODS TO CODE

# NOTE about Turtle coordinate axis.
# turtle centers the origin (x == 0, y == 0 ) in the center of the canvas
# so if our default screen size is : CANVAS_W, CANVAS_H = 800, 600
#  the corners of your screen are :
# Top-left: (-CANVAS_W/2, CANVAS_H/2) → (-400, 300)
# Top-right: ( CANVAS_W/2, CANVAS_H/2) → ( 400, 300)
# Bottom-left: (-CANVAS_W/2, -CANVAS_H/2) → (-400, -300)
# Bottom-right: ( CANVAS_W/2, -CANVAS_H/2) → ( 400, -300)


import turtle as T
import random

# ---------- constants ----------
CANVAS_W, CANVAS_H = 800, 600
TOP_MARGIN, BOTTOM_MARGIN = 40, 40

# size of houses
SIZES = {
    "s": (120, 80),
    "m": (150, 100),
    "l": (180, 120),
}

'''
How to use Themes : 
# Use a theme like this:
colors = THEMES[theme_key]          # where theme_key is either "pastel" or "primary"
body_c  = colors["body"]            # we then can access the colors for the body of the house
roof_c  = colors["roof"]            # color of the roof of the house 
door_c  = colors["door"]            # door 
win_c   = colors["window"]          # window -- feel free to add or change the colors 
                                    # there is are beautiful pallette choices at coolors.co

# how to apply :
fill_rect_center(cx, cy, w, h, body_c)  # house body
'''
THEMES = {
    "pastel": dict(body="#ffd1dc", roof="#c1e1c1", door="#b5d3e7", window="#fff7ae"),
    "primary": dict(body="red", roof="blue", door="gold", window="#aee3ff"),
}


# ---------- tiny turtle helpers (provided) ----------
def move_to(x, y):
    '''
    x - position on x coordinate axis
    y - position on y coordinate axis
    '''
    T.penup()
    T.goto(x, y)
    T.pendown()


def draw_line(x1, y1, x2, y2):
    '''
       we draw a line from x1,y1
       x1 - position on x coordinate axis
       y1 - position on y coordinate axis

       to x2, y2
       x2 - position on x coordinate axis
       y2 - position on y coordinate axis
       '''
    move_to(x1, y1)
    T.pendown()
    T.goto(x2, y2)
    T.penup()


def fill_rect_center(cx, cy, w, h, color):
    '''
    cx - center of rectangle x coordinate
    cy - center of rectangle y coordinate
    w - width of rectangle
    h - height of rectangle
    color - color of rectangle
    '''
    T.fillcolor(color)
    T.pencolor("black")
    move_to(cx - w / 2, cy + h / 2)
    T.begin_fill()
    for _ in range(2):
        T.forward(w)
        T.right(90)
        T.forward(h)
        T.right(90)
    T.end_fill()


def fill_triangle(p1, p2, p3, color):
    """
    Draw a filled triangle defined by three points.

    p1 — point 1 (x1, y1)
    p2 — point 2 (x2, y2)
    p3 — point 3 (x3, y3)
    color — fill color for the triangle

    Notes:
    - Each point is an (x, y) tuple.
    - Depending on your triangle, some x’s or y’s may be equal (e.g., flat base).

    Example:
    p1 = (x1, y1)
    p2 = (x2, y2)
    p3 = (x3, y3)
    fill_triangle(p1, p2, p3, color)
    """

    T.fillcolor(color)
    T.pencolor("black")
    move_to(*p1)
    T.begin_fill()
    T.goto(*p2)
    T.goto(*p3)
    T.goto(*p1)
    T.end_fill()


def fill_circle_center(cx, cy, r, color):
    '''
    a circle is defined by
    cx - the center of your circle, x coordinate
    cy - center of your circle, y coordinate
    r - radius
    color - color of circle
    '''
    T.fillcolor(color)
    T.pencolor("black")
    move_to(cx, cy - r)  # turtle draws circles from the bottom
    T.begin_fill()
    T.circle(r)
    T.end_fill()


# ---------- input helpers (complete; you may extend) ----------
def ask_choice_int(prompt, allowed):
    """Ask for an integer in the allowed set; reprompt on error.
        in a while loop, ask for a valid number from allowed list, exception is printed if incorrect number given,
        while loop continues until true

        prompt for :
        1. houses per roq
        2. how many houses
        """

    # a set is a list which only allows one unique item to exist, not any duplicates
    # if duplicates are given, set removes all duplicates
    allowed_set = set(allowed)
    while True:
        try:
            value = int(input(f"{prompt} {allowed}")) #added allowed to show user choices
            if value in allowed_set:
                return value
            else:
                print(f"Invalid number {value}. Must be in {allowed_set}.")
        except ValueError as e:
            print(f"Invalid input: {e}")


def ask_choice_str(prompt, allowed):
    """Ask for a string in the allowed list (case-insensitive); reprompt on error.
    in a while loop, ask for a valid string from allowed list, exception is printed if incorrect number given,
        while loop continues until true

        prompt for :
        1. house size
        2. color theme
        3. roof type
        4. sun
    """
    allowed_lower = [a.lower() for a in allowed]  # converting to lower case all in allowed list
    while True:
        try:
            value = str(input(f"{prompt} {allowed_lower}")) #added allowed to show user choices
            if value in allowed_lower:
                return value
            else:
                print(f"Invalid string {value}. Must be in {allowed_lower}.")
        except ValueError as e:
            print(f"Invalid input: {e}")



# ---------- TODO: draw_roads ----------
def draw_roads(cols, rows, cell_w, cell_h):
    """Draw straight separator lines between rows and columns (simple roads)."""
    # edges of the grid
    top_y = CANVAS_H / 2 - TOP_MARGIN
    bot_y = -CANVAS_H / 2 + BOTTOM_MARGIN
    left_x = -CANVAS_W / 2
    right_x = CANVAS_W / 2

    # TODO: set pen color + pensize
    T.pencolor("gray")
    T.pensize(3)
    # TODO: HORIZONTAL separators for r in 1..rows-1 at y = CANVAS_H/2 - TOP_MARGIN - r*cell_h
    #           here are are we vary y across rows (y = top_y - r*cell_h) and then
    #           drawing a line from (left_x, y) to (right_x, y)
    # drawing the roads between rows
    for r in range(1, rows):
        y = top_y - r * cell_h
        draw_line(left_x, y, right_x, y)
    # TODO: VERTICAL separators for c in 1..cols-1 at x = -CANVAS_W/2 + c*cell_w
    #           here we vary x across columns(x=left_x + c * cell_w) and
    #           then draw from (x, top_y) to(x, bot_y).
    # drawing rows between columns
    for c in range(1, cols):
        x = left_x + c * cell_w
        draw_line(x, top_y, x, bot_y)

# ---------- TODO: draw_house_centered ----------
def draw_house_centered(cx, cy, size_key, theme_key, roof_style):
    """Draw a simple house centered at (cx, cy)."""
    # width/height - getting house dimensions
    w, h = SIZES[size_key]
    colors = THEMES[theme_key]

    # TODO: body as centered rectangle
    fill_rect_center(cx, cy, w, h, colors["body"])
    # TODO: roof: if roof_style is a 'triangle' draw a triangle; otherwise draw a thin flat rectangle
    # figure out where top of the house is
    yT = cy + h / 2
    # to draw a triangle roof
    if roof_style == "triangle":
        p1 = (cx - w / 2, yT)
        p2 = (cx + w / 2, yT)
        p3 = (cx, yT + 0.5 * h)
        fill_triangle(p1, p2, p3, colors["roof"])
    # Suggestion is that the roof apex at (cx, yT + 0.5*h) where
    # to draw a flat roof
    else:
        roof_h = h * 0.1
        roof_cy = yT + roof_h / 2
        fill_rect_center(cx, roof_cy, w, roof_h, colors["roof"])
    # TODO: add a small door centered on x=cx
    door_w, door_h = w * 0.2, h * 0.4
    door_cy = cy - h * 0.3 # lower on the body
    fill_rect_center(cx, door_cy, door_w, door_h, colors["door"])
    # (optional) add one window off to the left


# ---------- TODO: draw_tree_near ----------
def draw_tree_near(cx, cy, size_key):
    """Draw a small tree near the house (left or right).
    Each trunk has a brown trunk with green circle on top"""

    # trunk
    w, h = SIZES[size_key]
    # trunk size (ratios)
    tw, th = w * 0.10, h * 0.40
    # place to left or right of the house randomly
    side = random.choice([-1, 1]) # -1 is left +1 is right
    tx = cx + side * (w * 0.45)
    ty = cy - h * 0.5 + th / 2
    # TODO: trunk: use fill_rect_center(tx, ty, tw, th, color)
    fill_rect_center(tx, ty, tw, th, "#8b5a2b")
    # TODO: canopy: use fill_circle_center(...) above trunk
    canopy_r = th * 0.6
    canopy_cy = ty + th / 2 + canopy_r * 0.7
    fill_circle_center(tx, canopy_cy, canopy_r, "forestgreen")


# ---------- TODO: draw_village (orchestration) ----------
def draw_village(cols, rows, size_key, theme_key, sun_flag, roof_style):
    """Compute cell sizes, draw roads, and loop over grid to place houses/trees.
    Drawing entire turtle village."""
    # calculate how much space each cell has
    cell_w = CANVAS_W / cols
    cell_h = (CANVAS_H - TOP_MARGIN - BOTTOM_MARGIN) / rows

    # TODO: draw roads first (so houses sit on top)
    draw_roads(cols, rows, cell_w, cell_h)
    # TODO: nested loops over r, c
    for r in range(rows):
        for c in range(cols):
            #   compute cx, cy (center per formulas). Center of cell.
            cx = -CANVAS_W / 2 + c * cell_w + cell_w / 2
            cy = CANVAS_H / 2 - TOP_MARGIN - r * cell_h - cell_h / 2
            #   draw_house_centered(...)
            draw_house_centered(cx, cy, size_key, theme_key, roof_style)
            #   draw_tree_near(...) giving 70% chance
            if random.random() < 0.7:
                draw_tree_near(cx, cy, size_key)


    # sun (optional) drawing in top right corner
    if sun_flag == 'y':
        r = 35
        cx = CANVAS_W / 2 - r - 20
        cy = CANVAS_H / 2 - r - 20
        fill_circle_center(cx, cy, r, "yellow")


# ---------- main ----------
def main():
    """Main program: asks the user for inputs, sets up the window, and draws everything."""
    print("Welcome to Turtle Village — Lite!")
    # gathering users input/choices
    cols = ask_choice_int("How many houses per row? ", [2, 3])
    rows = ask_choice_int("How many rows? ", [2])  # you may change to [2, 3]
    size_key = ask_choice_str("House size ", ["S", "M", "L"]).lower()
    theme_key = ask_choice_str("Color theme ", ["pastel", "primary"])
    roof_style = ask_choice_str("Roof type ", ["triangle", "flat"]).lower()
    sun_flag = ask_choice_str("Draw a sun? ", ["y", "n"]).lower()

    # window
    T.setup(CANVAS_W, CANVAS_H)
    T.speed(0)  # draw as fast as possible
    T.tracer(False)

    # the size of the property
    cell_w = CANVAS_W / cols
    cell_h = (CANVAS_H - TOP_MARGIN - BOTTOM_MARGIN) / rows

    # TODO: call draw_village with inputs
    draw_village(cols, rows, size_key, theme_key, sun_flag, roof_style)
    # TODO: finalize

    T.tracer(True)
    T.update()
    T.hideturtle()
    T.done()


if __name__ == "__main__":
    main()
