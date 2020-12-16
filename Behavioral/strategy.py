
class ImageDecoder(object):
    @staticmethod
    def decode(filename):
        raise NotImplementedError()


class PNGImageDecoder(ImageDecoder):
    @staticmethod
    def decode(filename):
        print('PNG decode')


class JPEGImageDecoder(ImageDecoder):
    @staticmethod
    def decode(filename):
        print('JPEG decode')


class GIFImageDecoder(ImageDecoder):
    @staticmethod
    def decode(filename):
        print('GIF decode')


class Image(object):
    @classmethod
    def open(cls, filename):
        ext = filename.rsplit('.', 1)[-1]
        if ext == 'png':
            decoder = PNGImageDecoder
        elif ext in ('jpg', 'jpeg'):
            decoder = JPEGImageDecoder
        elif ext == 'gif':
            decoder = GIFImageDecoder
        else:
            raise RuntimeError(f'Error type of file :{filename}')
        byterange = decoder.decode(filename)
        return cls(byterange, filename)

    def __init__(self, byterange, filename):
        self._byterange = byterange
        self._filename = filename


Image.open('picture.png')
Image.open('picture.jpg')
Image.open('picture.gif')