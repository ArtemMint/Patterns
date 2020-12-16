class Subject(object):
    """Class subject"""
    def __init__(self):
        self._data = None
        self._observers = set()

    def attach(self, observer):
        # подписаться на оповещение
        if not isinstance(observer, ObserverBase):
            raise TypeError()
        self._observers.add(observer)

    def detach(self, observer):
        # отписаться от оповещения
        self._observers.remove(observer)

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data
        self.notify(data)

    def notify(self, data):
        # уведомить всех наблюдателей о событии
        for observer in self._observers:
            observer.update(data)


class ObserverBase(object):
    """Abstract observer"""
    def update(self, data):
        raise NotImplementedError()


class Observer(ObserverBase):
    """Class observer"""
    def __init__(self, name):
        self._name = name

    def update(self, data):
        print (f'{self._name}: {data}')


subject = Subject()
subject.attach(Observer('Observer 1'))
subject.attach(Observer('Observer 2'))
subject.set_data('data about observer')