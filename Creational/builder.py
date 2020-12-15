class Director:

    def __init__(self):
        print('Director was init')
        self.builder = None

    def construct(self, builder):
        self.builder = builder
        self.builder._build_part_a()
        self.builder._build_part_b()
        self.builder._build_part_c()

class Builder():

    def __init__(self):
        print('Builder was init')
        self.product = House()

    def _build_part_a(self):
        print('Start to build a foundation...')
        self.product.set_foundation()

    def _build_part_b(self):
        print('Start to build a walls...')
        self.product.set_walls()

    def _build_part_c(self):
        print('Start to build a roof...')
        self.product.set_roof()


class House():

    def __init__(self):
        print('Plan of house was init')
        self.foundation = None
        self.wals = None
        self.roof = None

    def set_foundation(self):
        self.foundation = 'One foundation'
        print('... the foundation is built')

    def set_walls(self):
        self.wals = 'Four walls'
        print('... the walls is built')

    def set_roof(self):
        self.roof = 'One roof'
        print('... the roof is built')

def main():
    director = Director()
    builder = Builder()
    director.construct(builder)
    product = builder.product
    print(f'House constructed with :{product.roof},{product.wals},{product.foundation}')

if __name__ == '__main__':
    main()