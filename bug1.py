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
        return (
            f"({self.x}, {self.y})\n"
            f"{self.size}\n"
            "        , - ~ ~ ~ - ,\n"
            "    , '               ' ,\n"
            "  ,                       ,\n"
            " ,                         ,\n"
            ",                           ,\n"
            ",                           ,\n"
            ",                           ,\n"
            " ,                         ,\n"
            "  ,                       ,\n"
            "    ,                   ,\n"
            "        - , _ _ _ , '\n"
        )
    
def main():
    c = Circle(1, 2, 3)
    print(c.shape())
    print(c.draw())

main()