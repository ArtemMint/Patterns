class Singleton(object):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            print('Creating new instance of class...')
            cls.__instance = super(Singleton, cls).__new__(cls)
        else:
            print('Class already has instance')
        return cls.__instance


def main():
    instance1 = Singleton()
    instance2 = Singleton()
    instance3 = Singleton()
    print('True' if id(instance1) == id(instance2) else False)
    print('True' if id(instance1) == id(instance3) else False)

if __name__ == '__main__':
    main()