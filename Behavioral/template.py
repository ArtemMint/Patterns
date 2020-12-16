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


class Example(ExampleBase):
    def step_one(self):
        print('First step')

    def step_two(self):
        print('Second step')

    def step_three(self):
        print('Third step')


example = Example()
example.template_method()