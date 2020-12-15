import copy

class Prototype:
    """
    Example class to be copied.
    """
    def clone(self):
        pass

class MyObject(Prototype):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def clone(self):
        return copy.deepcopy(self)


def main():
    prototype = MyObject('Max','max@gmail.com')
    prototype_copy = prototype.clone()
    print(f'First instance - {prototype.name}, {prototype.email}')
    print(f'Second instance - {prototype_copy.name}, {prototype_copy.email}')

if __name__ == "__main__":
    main()