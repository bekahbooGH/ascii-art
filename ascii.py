# # 0123456789
# #0 
# #1 ***   *** 
# #2 * *   * *
# #3 ***   ***
# #4 
# #5 =========
# #6 =       = 
# #7 ========= 
# #8 


class Canvas():
  def __init__(self, height, width, empty='.'):
    # self.data = [[empty]*width for _ in range(height)]
    self.height = height
    self.width = width
    self.empty = empty
    self.shapes = []

  def add(self, shape):
    self.shapes.append(shape)

  def clear(self):
    self.shapes = []

  def render(self):
    data = [[self.empty]*self.width for _ in range(self.height)]
    for shape in self.shapes:
      shape.fill(data)
    for row in data:
      print(''.join(row))

  def zoom_in(self, zoom):
    zoom_data = [[self.empty]*(self.width*zoom) for _ in range((self.height*zoom))]
    for shape in self.shapes:

      if shape.start_x < shape.start_y:
        shape.start_x = shape.start_x
        shape.start_y = shape.end_y - zoom + 1
      elif shape.start_y < shape.start_x:
        shape.start_y = shape.start_y
        shape.start_x = shape.end_x - zoom + 1
      shape.end_x - shape.start_x + 1
      shape.end_y - shape.start_y + 1
      shape.end_x = shape.end_x * zoom
      shape.end_y = shape.end_y * zoom
      shape.fill_char = shape.fill_char


class Rectangle():
  def __init__(self, start_x, start_y, end_x, end_y, fill_char):
    self.start_x = start_x
    self.start_y = start_y
    self.end_x = end_x
    self.end_y = end_y
    self.fill_char = fill_char

  def __repr__(self):
    return (
        f'Rectangle({self.start_x}, {self.start_y}, {self.end_x}, '
        f'{self.end_y}, {repr(self.fill_char)})')

  def fill(self, data):
    for y in range(self.start_y, self.end_y+1):
      for x in range(self.start_x, self.end_x+1):
        data[y][x] = self.fill_char
  
  def change_char(self, char):
    self.fill_char = char

  def translate(self, axis, nums):
    if axis == 'y': #up or down
      self.start_y += nums
      self.end_y += nums
    elif axis == 'x': #left or right
      self.start_x += nums
      self.end_x += nums


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

print(c.shapes)
rectangles[0].translate('y', 1)
rectangles[3].translate('y', 1)
c.render()
rectangles[2].change_char('_')
c.render()
print(c.shapes)

# *********INVERTED CANVAS - ON RECTANGLE.FILL()*********
# # 0123456789
# #8 
# #7 ***   *** 
# #6 * *   * *
# #5 ***   ***
# #4 
# #3 =========
# #2 =       = 
# #1 ========= 
# #0 


# class Canvas():
#   def __init__(self, height, width, empty='.'):
#     # self.data = [[empty]*width for _ in range(height)]
#     self.height = height
#     self.width = width
#     self.empty = empty
#     self.shapes = []

#   def add(self, shape):
#     self.shapes.append(shape)

#   def clear(self):
#     self.shapes = []

#   def render(self):
#     data = [[self.empty]*self.width for _ in range(self.height)]
#     for shape in self.shapes:
#       shape.fill(data)
#     for row in data:
#       print(''.join(row))


# class Rectangle():
#   def __init__(self, start_x, start_y, end_x, end_y, fill_char):
#     self.start_x = start_x
#     self.start_y = start_y
#     self.end_x = end_x
#     self.end_y = end_y
#     self.fill_char = fill_char

#   def __repr__(self):
#     return (
#         f'Rectangle({self.start_x}, {self.start_y}, {self.end_x}, '
#         f'{self.end_y}, {repr(self.fill_char)})')

#   def fill(self, data):
#     max_y = len(data) - 1
#     for y in range(self.start_y, self.end_y+1):
#       for x in range(self.start_x, self.end_x+1):
#         data[max_y - y][x] = self.fill_char
  
#   def change_char(self, char):
#     self.fill_char = char

#   def translate(self, axis, nums):
#     if axis == 'y': #up or down
#       self.start_y += nums
#       self.end_y += nums
#     elif axis == 'x': #left or right
#       self.start_x += nums
#       self.end_x += nums


# c = Canvas(9, 10)
# rectangles = [
#   Rectangle(1, 5, 3, 7, '*'),
#   Rectangle(7, 5, 9, 7, '*'),
#   Rectangle(1, 1, 9, 3, '='),
#   Rectangle(2, 6, 2, 6, ' '),
#   Rectangle(8, 6, 8, 6, ' '),
#   Rectangle(2, 2, 8, 2, ' '),
#   ]
# for r in rectangles:
#   c.add(r) 
# c.render()

# print(c.shapes)
# rectangles[0].translate('y', 1)
# rectangles[3].translate('y', 1)
# c.render()
# rectangles[2].change_char('_')
# c.render()
# print(c.shapes)

# *********INVERTED CANVAS - ON CANVAS.RENDER()**********
# 0123456789
#8 
#7 ***   *** 
#6 * *   * *
#5 ***   ***
#4 
#3 =========
#2 =       = 
#1 ========= 
#0 

# class Canvas():
#   def __init__(self, height, width, empty='.'):
#     # self.data = [[self.empty]*self.width for i in range(self.height)]
#     self.height = height
#     self.width = width
#     self.empty = empty
#     self.shapes = []

#   def add(self, shape):
#     self.shapes.append(shape)

#   def clear(self):
#     self.shapes = []

#   def render(self):
#     self.data = [[self.empty]*self.width for _ in range(self.height)]
#     for shape in self.shapes:
#       shape.fill(self) #something here? why wont the rectangle print at like (1,1) instead of still printing at the old location (7,1).
#     for row in self.data:
#       print(''.join (row))

#   def set_pixel(self, x, y, val):
#     if 0 <= x < self.width and 0 <= y < self.height:
#       self.data[self.height - y - 1][x] = val


# class Rectangle():
#   def __init__(self, start_x, start_y, end_x, end_y, fill_char):
#     self.start_x = start_x
#     self.start_y = start_y
#     self.end_x = end_x
#     self.end_y = end_y
#     self.fill_char = fill_char

#   def __repr__(self):
#     return (
#         f'Rectangle({self.start_x}, {self.start_y}, {self.end_x}, '
#         f'{self.end_y}, {repr(self.fill_char)})')

#   def fill(self, canvas):
#     for y in range(self.start_y, self.end_y+1): 
#       for x in range(self.start_x, self.end_x+1): 
#         canvas.set_pixel(x, y, self.fill_char)
        

#   def change_char(self, char):
#     self.fill_char = char

#   def translate(self, axis, nums):
#     if axis == 'y': #up or down
#       self.start_y += nums
#       self.end_y += nums
#     elif axis == 'x': #left or right
#       self.start_x += nums
#       self.end_x += nums

# c = Canvas(9, 10)
# rectangles = [
#   Rectangle(1, 5, 3, 7, '*'),
#   Rectangle(7, 5, 9, 7, '*'),
#   Rectangle(1, 1, 9, 3, '='),
#   Rectangle(2, 6, 2, 6, ' '),
#   Rectangle(8, 6, 8, 6, ' '),
#   Rectangle(2, 2, 8, 2, ' '),
#   ]
# for r in rectangles:
#   c.add(r) 
# c.render()

# print(c.shapes)
# rectangles[0].translate('y', 1)
# rectangles[3].translate('y', 1)
# c.render()
# rectangles[2].change_char('_')
# c.render()
# print(c.shapes)


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

