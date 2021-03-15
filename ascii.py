## Specifications

class ASCII_Canvas():
  def __init__(self, height=0, width=0):
    self.height = height
    self.width = width

# def build_board(cols, rows, sp=2):
#     board = []
#     l = len(str(cols * rows)) + sp
#     for i in range(1, cols * rows + 1):
#         board.append(i)
#         print('{0:>{1}}'.format(i, l), end='')
#         if i % cols == 0:
#             print()
#     return board

# build_board(8, 17, 3)

# for row in board:
#     for column in row:
#         print(column, end=' ')
#     print()

  def print_Canvas(self):
    l_ = []
    for i in range(self.height-1, self.height):
      for j in range(self.width):
        # if i == (self.height-1):
        l_.append('__')
    for i in range(0, self.height-1):
      if i % 9 == 0:
        l_.append('  ')
      else:
        l_.append('|')
    # for i in range(1): #I want to do like the min and max = so at 0 and 10
    #   l_.append('__')
      

    for i in range(self.height):
      for j in range(1):
        l_.append('|') #I want to do like the min and max = so at 0 and 10
      for i in range((self.width-1), self.width):
        l_.append('|')

    joined_l = ''.join(l_)
    for i, char in enumerate(joined_l):
      print('{char}'.format(i), end='')
      # print(char)
      # if i % 10 == 0:
      #   print('\n')
    # print(len(joined_l))
    # print(joined_l)
    # for char in l_:
    #   if char % 10 == 0:
    #     \n

#     board = []
# for i in range(1,43):
#     board.append(i)
#     print('{:>4}'.format(i), end='')
#     if i % 6 == 0:
#         print()

  # def clear_all_shapes(self):
  #   for i in range(1):
  #     for j in range(1, self.width-1):
  #       # if something is there:
  #       # make it none

class Rectangle():
  def __init__(self, height=0, width=0):
    self.height = height
    self.width = width
          

  def render_to_canvas(self, x_start=0, y_start=0, x_end=0, y_end=0, char="-"):
      self.x_start = x_start
      self.y_start = y_start
      self.x_end = x_start
      self.y_end = y_start
      self.char = char

  def change_char(self, char="-"):
      self.char = char

canvas = ASCII_Canvas(10, 10)
rectangle1 = Rectangle(5, 3)
canvas.print_Canvas()

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

