import weakref


class Color(object):
    """Class flyweight"""
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name

class ColorFactory(object):
    """Class factory of flyweight"""
    _colors = weakref.WeakValueDictionary()

    @classmethod
    def get_color(cls, name):
        value = cls._colors.get(name)
        if value is None:
            value = Color(name)
            cls._colors[name] = value
        return value

class Placemark(object):
    """Class placemark"""
    def __init__(self, latitude, longitude, color_name):
        self._latitude = latitude
        self._longitude = longitude

        self._color = ColorFactory.get_color(color_name)

    def __str__(self):
        return(f'Color: {self._color}; Coordinate: ({self._latitude}, {self._longitude})')

def main():
    mark1 = Placemark(-73.237221, 25.714551, 'green')
    mark2 = Placemark(73.617761, 80.755773, 'green')
    mark3 = Placemark(72.473761, 120.752323, 'red')


    print(mark1)
    print(mark2)
    print(mark3)

    print(mark1._color is mark2._color)
    print(mark2._color is mark3._color)

if __name__ == '__main__':
    main()

