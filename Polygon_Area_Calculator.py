class Rectangle():
    def __init__(self,width,height):
      self.width = width
      self.height = height

    def __str__(self):
      return(f"Rectangle(width={self.width}, height={self.height})")

    def set_width(self,cwidth):
      self.width = cwidth
    def set_height(self,cheight):
      self.height = cheight

    def get_area(self):
      return self.width * self.height
    def get_perimeter(self):
      return 2*self.width + 2*self.height
    def get_diagonal(self):
      return(self.width**2 + self.height**2)**0.5

    def get_picture(self):
      if self.width > 50 or self.height > 50:
        return('Too big for picture.')
      line = "*" * self.width
      pic = ""
      for i in range (self.height):
        pic += line
        pic += "\n"
      return(pic)
    def get_amount_inside(self,shape):
      w=shape.width
      h=shape.height
      return (self.width//w * self.height//h)


class Square(Rectangle):
    def __init__(self,side):
      super().__init__(side,side)
    def __str__(self):
      return(f'Square(side={self.width})')

    def set_side(self,side):
      self.width = side
      self.height = side
    def set_width(self,side):
      self.set_side(side)
    def set_height(self,side):
      self.set_side(side)
      
rect = Rectangle(1,2)
rect.set_width(9)
rect.set_height(3)

print(rect.get_area())
print(rect)
print(rect.get_picture())

print ("-----------------")

sq = Square(2)
print(sq)
print(sq.get_perimeter())
print(sq.get_picture())

print(Rectangle(15,10).get_amount_inside(Square(5)))