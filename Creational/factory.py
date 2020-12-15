class Product:
    def some_func(self):
        pass

class Worker(Product):
    def __init__(self, name, age, hours):
        self.name = name
        self.age = age
        self.hours = hours

    def __str__(self):
        return self.name+" ["+str(self.age)+"] - "+str(self.hours)+"h/week"

class Unemployed(Product):
    def __init__(self, name, age, able):
        self.name = name
        self.age = age
        self.able = able

    def __str__(self):
        if self.able:
            return self.name+" ["+str(self.age)+"] - able to work"
        else:
            return self.name+" ["+str(self.age)+"] - unable to work"

class PersonFactory:
    def get_person(self, type_of_person):
        if type_of_person == "worker":
            return Worker("Oliver", 22, 30)
        if type_of_person == "unemployed":
            return Unemployed("Mark", 33, False)

def main():
    factory = PersonFactory()
    product = factory.get_person("worker")
    print(product)
    product2 = factory.get_person("unemployed")
    print(product2)

if __name__ == '__main__':
    main()
#полиморфизм
#дебагер
#Git / PyCharm