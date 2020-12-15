class Product():
    """
    Class Product
    """
    def cook(self):
        pass

class FettuccineAlfredo(Product):
    """
    Class italian main dish
    """
    name = "Fettuccine Alfredo"

    def cook(self):
        print("Italian main course prepared: "+self.name)

class Tiramisu(Product):
    '''
    Class italian dessert
    '''
    name = "Tiramisu"

    def cook(self):
        print("Italian dessert prepared: "+self.name)

class DuckALOrange(Product):
    '''
    Class french main dish
    '''
    name = "Duck À L'Orange"

    def cook(self):
        print("French main course prepared: "+self.name)

class CremeBrulee(Product):
    '''
    Class french dessert
    '''
    name = "Crème brûlée"

    def cook(self):
        print("French dessert prepared: "+self.name)

class AbstractFactory():
    '''
    Abstract factory
    '''
    def get_dish(type_of_meal):
        pass

class ItalianDishesFactory(AbstractFactory):
    '''
    Italian factory method
    '''
    def get_dish(type_of_meal):
        if type_of_meal == "main":
            return FettuccineAlfredo()
        if type_of_meal == "dessert":
            return Tiramisu()

    def create_dessert(self):
        return Tiramisu()

class FrenchDishesFactory(AbstractFactory):
    '''
    French factory method
    '''
    def get_dish(type_of_meal):
        if type_of_meal == "main":
            return DuckALOrange()
        if type_of_meal == "dessert":
            return CremeBrulee()

class FactoryProducer:
    '''
    Class factory producer
    '''
    def get_factory(self, type_of_factory):
        if type_of_factory == "italian":
            return ItalianDishesFactory
        if type_of_factory == "french":
            return FrenchDishesFactory


def main():
    fp = FactoryProducer()
    factory = fp.get_factory('french')
    main_dish = factory.get_dish('main')
    main_dish.cook()
    factory = fp.get_factory('italian')
    main_dish = factory.get_dish('dessert')
    main_dish.cook()


if __name__ == '__main__':
    main()