class SingletonMeta(type):

    __instance = {}


    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super().__call__(*args, **kwargs)
        return cls.__instance


class Singleton(metaclass=SingletonMeta):

    def some_func(self):
        pass

def main():
    instance1 = Singleton()
    instance2 = Singleton()
    instance3 = Singleton()
    print('True' if id(instance1) == id(instance2) else False)
    print('True' if id(instance1) == id(instance3) else False)

if __name__ == '__main__':
    main()