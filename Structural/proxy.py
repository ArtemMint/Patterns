class ImageBase(object):
    """Abstract image"""
    @classmethod
    def create(cls, width, height):
        """Create size of image"""
        return cls(width, height)

    def draw(self, x, y, color):
        """Drawwing point with color"""
        raise NotImplementedError()

    def fill(self, color):
        """Fill image with color"""
        raise NotImplementedError()

class Image(ImageBase):
    """Class Image"""
    def __init__(self, width, height):
        self._width = int(width)
        self._height = int(height)

    def draw(self, x, y, color):
        print(f'Drawwing point; coordinate: ({x}, {y}); color: {color}')

    def fill(self, color):
        print(f'Fill color: {color}')


class ImageProxy(ImageBase):
    """
    Class ImageProxy. Control class Image.
    """
    def __init__(self, *args, **kwargs):
        self._image = Image(*args, **kwargs)

    def draw(self, *args):
        print('Starting function draw...')
        self._image.draw(*args)

    def fill(self, *args):
        print('Fill image...')
        self._image.fill(*args)


def  main():
    img = ImageProxy(500, 500)
    img.fill('yellow')
    img.draw(0, 0, 'green')
    img.draw(1, 1, 'red')

if __name__ == '__main__':
    main()


"""
Например, проверка авторизации пользователя для получения доступа к его хранилищу
Кеширование одинаковых запросов.
"""