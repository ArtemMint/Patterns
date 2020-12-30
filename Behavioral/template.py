class ExampleBase(object):
    def template_method(self):
        self.step_one()
        self.step_two()
        self.step_three()

    def step_one(self):
        raise NotImplementedError()

    def step_two(self):
        raise NotImplementedError()

    def step_three(self):
        raise NotImplementedError()


class Example1(ExampleBase):
    def step_one(self):
        print('First step')

    def step_two(self):
        print('Second step')

    def step_three(self):
        print('Third step')

class Example2(ExampleBase):
    def step_one(self):
        print('Another first step')

    def step_two(self):
        print('Another second step')

    def step_three(self):
        print('Another third step')


example = Example1()
example.template_method()
print('\n')
example = Example2()
example.template_method()

"""
Разные алгоритмы чтения документов.
"""