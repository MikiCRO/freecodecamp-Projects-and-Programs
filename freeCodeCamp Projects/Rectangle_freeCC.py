class Rectangle():
    def __init__(self,width,height):
        self._width = width
        self._height = height
        self._side = width
        self._side = height
    
    def __str__(self):
        return (f"Rectangle(width={self._width}, height={self._height})")
        
    def set_width(self,value):
        self._width = value
        self._side = value
        return self._width
        
    def set_height(self,height):
        self._height = height
        self._side = height
        return self._height
        
    def get_area(self):
        return self._width * self._height
    
    def get_perimeter(self):
        return (2*self._width) + (self._height * 2)
        
        
    def get_diagonal(self):
        return ((self._width ** 2) + (self._height ** 2)) ** .5
    
    def get_picture(self):
        if self._width > 50 or self._height >50:
            return f"Too big for picture."
        else:
            z = self._width * "*" 
            z = z + "\n"
            z = z*self._height
            # z = z.rstrip()
            return z
    
    
    def get_amount_inside(self,instance):
        # print(self._width)
        # print(self._height)
        # print(sq._side)
        sirina = self._width // instance._side
        duzina = self._height // instance._side
        
        if sirina == 0 and duzina != 0:
            return duzina
        elif duzina == 0 and sirina != 0:
            return sirina
        elif sirina == 0 and duzina == 0:
            return 0
        else:
        
            return sirina * duzina
        
class Square(Rectangle):
    
    def __init__(self,side):
        self._side = side
        
        super().__init__(width=self._side,height=self._side)
        
    def set_side(self,side):
        self._width = side
        self._height = side
        self._side = side
        
        return self._side
    
        
        
    def __str__(self):
        return (f"Square(side={self._side})")


    
        
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
print(sq)
        
        
        
            
        
            
