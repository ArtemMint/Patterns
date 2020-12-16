class HttpHandler(object):
    """Abstract class"""
    def handle(self, code):
        raise NotImplementedError()


class Http404Handler(HttpHandler):
    """Code 404"""
    def handle(self, code):
        if code == 404:
            return 'Page not found'


class Http500Handler(HttpHandler):
    """Code 500"""
    def handle(self, code):
        if code == 500:
            return 'Server error'


class Client(object):
    def __init__(self):
        self._handlers = []

    def add_handler(self, h):
        self._handlers.append(h)

    def response(self, code):
        for h in self._handlers:
            msg = h.handle(code)
            if msg:
                print(f'Answer: {msg}')
                break
        else:
            print('Сode not processed')


def main():
    client = Client()
    client.add_handler(Http404Handler())
    client.add_handler(Http500Handler())
    client.response(400)
    client.response(404)
    client.response(500)

if __name__ == '__main__':
    main()