class AbstractionSort:

    def sortImpl(self, sortImpl):
        self._sortImpl = sortImpl

    def sort(self, data):
        self._sortImpl.sort(data)
        return data

class Sort:

    def sort(self, data):
        pass

class FastSort(Sort):

    def sort(self, data):
        return data.sort()

class SlowSort(Sort):

    def sort(self, data):
        return data.sort()


if __name__ == '__main__':
    interface = AbstractionSort()

    interface.sortImpl(SlowSort())
    print(interface.sort([2, 1, 3]))

    interface.sortImpl(FastSort())
    print(interface.sort([2, 1, 3]))



"""
Разделение интерфейса от реализации управления различными БД.
"""