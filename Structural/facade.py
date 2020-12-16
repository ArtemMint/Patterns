class Paper(object):
    """Class paper"""
    def __init__(self, count):
        self._count = count

    def get_count(self):
        return self._count

    def draw(self, text):
        if self._count > 0:
            self._count -= 1
            print(text)

class Printer(object):
    """Class printer"""
    def error(self, msg):
        print(f'Error: {msg}')

    def print_(self, paper, text):
        if paper.get_count() > 0:
            paper.draw(text)
        else:
            self.error('Not enough paper')

class Facade(object):
    def __init__(self):
        self._printer = Printer()
        self._paper = Paper(1)

    def write(self, text):
        self._printer.print_(self._paper, text)

def main():
    f = Facade()
    f.write('First text!')
    f.write('Second text!')

if __name__ == '__main__':
    main()