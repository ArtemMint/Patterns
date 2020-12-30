class FruitVisitor(object):
    """Visitor"""
    def draw(self, fruit):
        methods = {
            Apple: self.draw_apple,
            Pear: self.draw_pear,
        }
        draw = methods.get(type(fruit), self.draw_unknown)
        draw(fruit)

    def draw_apple(self, fruit):
        print('Drawing an apple')

    def draw_pear(self, fruit):
        print('Drawing a pear')

    def draw_unknown(self, fruit):
        print('Drawing some fruit')

class Fruit(object):
    """Class Fruit"""
    def draw(self, visitor):
        visitor.draw(self)

class Apple(Fruit):
    """Apple"""

class Pear(Fruit):
    """Pear"""

class Banana(Fruit):
    """Banana"""

if __name__ == '__main__':
    visitor = FruitVisitor()

    apple = Apple()
    apple.draw(visitor)

    pear = Pear()
    pear.draw(visitor)

    banana = Banana()
    banana.draw(visitor)

"""
Експорт обьектов в XML
"""