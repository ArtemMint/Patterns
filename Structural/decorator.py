class Human():
    """Class human"""
    def __init__(self, name):
        self._name = name

    def say(self):
        print(f'Hello! My name is {self._name}')

class Fish():
    """Class fish"""
    def __init__(self, name):
        self._name = name

    def say(self):
        print(f'Fish name is - {self._name}')

class Plan:
    """Class Plan"""
    def __init__(self, human):
        self._human = human

    def __getattr__(self, item):
        return getattr(self._human, item)

    def fly(self):
        print(f'{self._human._name} fly on the plan.')

def main():
    man = Human('James')
    fish = Fish('Bob')
    plan = Plan(man)
    plan.say()
    plan.fly()
    plan = Plan(fish)
    plan.say()
    plan.fly()

if __name__ == '__main__':
    main()

