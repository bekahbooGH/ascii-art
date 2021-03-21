# 0123456789
#0 
#1 ***   *** 
#2 * *   * *
#3 ***   ***
#4 
#5 =========
#6 =       = 
#7 ========= 
#8 


class Canvas():
  def __init__(self, height, width, empty='.'):
    self.data = [[empty]*width for _ in range(height)]
    self.shapes = []

  def add(self, shape):
    self.shapes.append(shape)

  def clear(self):
    self.shapes = []

  def render(self):
    for shape in self.shapes:
      shape.render(self.data)
    for row in self.data:
      print(''.join(row))


class Rectangle():
  def __init__(self, start_x, start_y, end_x, end_y, fill_char):
    self.start_x = start_x
    self.start_y = start_y
    self.end_x = end_x
    self.end_y = end_y
    self.fill_char = fill_char

  def render(self, data):
    for x in range(self.start_x, self.end_x+1):
      for y in range(self.start_y, self.end_y+1):
        data[y][x] = self.fill_char
  
  def change_char(self, char):
    self.fill_char = char

  def translate(self, axis, nums):
    if axis == 'y': #up or down
      if nums < 0:
        pass
        # shift down, x start/end stays the same
      else:
        pass
        # shift up, x start/end stays the same

    elif axis == 'x': #left or right
      if nums < 0:
        pass
        # shift left, y start/end stays the same
      else:
        pass
        # shift right, y start/end stays the same
    
    pass

c = Canvas(9, 10)
rectangles = [
  Rectangle(1, 1, 3, 3, '*'),
  Rectangle(7, 1, 9, 3, '*'),
  Rectangle(1, 5, 9, 7, '='),
  Rectangle(2, 2, 2, 2, ' '),
  Rectangle(8, 2, 8, 2, ' '),
  Rectangle(2, 6, 8, 6, ' '),
  ]
for r in rectangles:
  c.add(r) 

c.render()

# You'll be in charge of implementing the API for drawing **rectangles** (and
# squares). The API must be able to:

# - Render canvas with a specified height and width
#   - Print the canvas and any shapes to standard output
# - Add a shape to a canvas
#   - **_shape_** the shape to add. For now, assume you only have to deal
#     with rectangles
# - Clear all shapes from a canvas
# - Create a rectangle
#   - **_start_x_** is the X coordinate of the upper-left-hand corner of the
#     rectangle
#   - **_start_y_** is the Y coordinate of the upper-left-hand corner of the
#     rectangle
#   - **_end_x_** is the X coordinate of the lower-right-hand corner of the
#     rectangle
#   - **_end_y_** is the Y coordinate of the lower-right-hand corner of the
#     rectangle
#   - **_fill_char_** is the character that should be used to draw the
#     rectangle
# - Change a rectangle's fill character
#   - **_char_** the character to use in order to draw a pre-existing
#     rectangle
# - Translate (move left, right, up, or down)
#   - **_axis_** which axis (`'x'` or `'y'`) should we translate the rectangle on?
#     Translating on the X-axis will cause the rectangle to move left
#     and right. Translating on the Y-axis will cause the rectangle to
#     move up and down.
#   - **_num_** is how much to move the rectangle. Negative numbers will
#     cause the rectangle to shift left or down. Positive numbers will cause
#     the rectangle to shift right or up.

# ## Notes

# Rectangles can overlap with one another. The most recently added rectangle
# should appear on top of other rectangles. For example:

# ```
#  ++++
#  ++.....
#  ++.....
#    .....




# ```

# Make sure you do not render any characters that are out of bounds.

# Feel free to make decisions/assumptions about things you have questions about and please document these decisions (using comments in your solution is fine).

