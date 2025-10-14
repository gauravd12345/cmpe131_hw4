class Base:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

class Circle(Base):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)

    def shape(self):
        return "This is a circle"
    
    def draw(self):
        return f"""
({self.x}, {self.y})\n{self.size}
                , - ~ ~ ~ - ,
            , '               ' ,
         ,                         ,
       ,                             ,
      ,                               ,
     ,                                 ,
     ,                                 ,
      ,                               ,
       ,                             ,
         ,                         ,
            , '               ' ,
                ' - , - - - , '
                      """
    
# def main():
#     c = Circle(2, 2, 3)
#     print(c.shape())
#     print(c.draw())

# main()
