class Graphic(object):
    def draw(self):
        raise NotImplementedError()

    def add(self, obj):
        raise NotImplementedError()

    def remove(self, obj):
        raise NotImplementedError()

    def get_child(self, index):
        raise NotImplementedError()


class Line(Graphic):
    def draw(self):
        print('Line')


class Rectangle(Graphic):
    def draw(self):
        print('Rectangle')


class Text(Graphic):
    def draw(self):
        print('Text')


class Picture(Graphic):
    def __init__(self):
        self._list = []

    def draw(self):
        print('Picture')
        for obj in self._list:
            obj.draw()

    def add(self, obj):
        if isinstance(obj, Graphic) and not obj in self._list:
            self._list.append(obj)

    def remove(self, obj):
        index = self._list.index(obj)
        del self._list[index]

    def get_list(self, index):
        return self._list[index]

def main():
    pic = Picture()
    pic.add(Line())
    pic.add(Rectangle())
    pic.add(Text())
    pic.draw()


if __name__ == '__main__':
    main()

"""
Меню сайта
"""