"""
P-2.39: Develop an inheritance hierarchy based upon a Polygon class that has abstract methods area( ) and perimeter( ). 
In order to avoid less trivial math, let's just Implement classes RightTriangle, Square and Rectangle.
"""

from abc import ABC, abstractmethod
import math
 
class Polygon(ABC):
  
  @abstractmethod
  def area(self):
    pass

  @abstractmethod
  def perimeter(self):
    pass

class RightTriangle(Polygon):

  def __init__(self, base, height):
    self.base = base
    self.height = height

  def area(self):
    return 0.5 * self.base * self.height
  
  def perimeter(self):
    hypotenuse = self.base**2 + self.height**2
    return self.base + self.height + math.sqrt(hypotenuse)
  
class Rectangle (Polygon):
  
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def area(self):
    return self.width * self.height
  
  def perimeter(self):
    return (self.width + self.height) * 2
  
class Square (Rectangle):
  
  def __init__(self, side):
    super().__init__(side, side)


if __name__ == "__main__":
  
    # create a right triangle with base 3 and height 4
    rt = RightTriangle(3, 4)
    print("Right Triangle area:", rt.area())
    print("Right Triangle perimeter:", rt.perimeter())
 
    # create a rectangle with width 3 and height 4
    rect = Rectangle(3, 4)
    print("Rectangle area:", rect.area())
    print("Rectangle perimeter:", rect.perimeter())
 
    # create a square with side 3
    sq = Square(3)
    print("Square area:", sq.area())
    print("Square perimeter:", sq.perimeter()) 