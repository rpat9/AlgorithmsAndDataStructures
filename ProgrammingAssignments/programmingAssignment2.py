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
    return 0.5*self.base*self.height
  
  def permieter(self):
    hypotenuse = self.base**2 + self.height**2
    return self.base+self.height+math.sqrt(hypotenuse)